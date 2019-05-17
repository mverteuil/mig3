from unittest import mock

from django.utils.decorators import classproperty

from model_mommy import mommy

from . import models as wizard


def test_stages_metaclass():
    """Should attach STAGES list to class, with stages in the order they are defined."""
    # noqa: D202
    class ClassWithStages(metaclass=wizard.SetupProgressStagesMeta):
        @classproperty
        def a(self):
            pass

        @classproperty
        def b(self):
            pass

        def c(self):
            pass

        @classmethod
        def d(cls):
            pass

        @staticmethod
        def e():
            pass

    assert ClassWithStages.STAGES == ["a", "b"]


def test_no_progress(db):
    """All stages should be negative at the beginning."""
    for stage in wizard.SetupProgress.STAGES:
        assert getattr(wizard.SetupProgress, stage) is False


def test_has_administrator(admin_user):
    """Should detect administrator and next stage."""
    assert wizard.SetupProgress.has_administrator
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_administrator") + 1


def test_has_builder(admin_user, builder_account):
    """Should detect builder and next stage."""
    assert wizard.SetupProgress.has_builder
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_builder") + 1


def test_has_project(admin_user, builder_account, project):
    """Should detect builder and next stage."""
    assert wizard.SetupProgress.has_builder
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_project") + 1


def test_has_targets_without_enough(admin_user, builder_account, primary_target, project):
    """Should require two project targets."""
    assert not wizard.SetupProgress.has_targets
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_targets")


def test_has_targets_without_enough_for_same_project(admin_user, builder_account, primary_target, project):
    """Should require two targets attached to the same project."""
    mommy.make("projects.Target")
    assert not wizard.SetupProgress.has_targets
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_targets")


def test_has_targets(admin_user, builder_account, primary_target, project, secondary_target):
    """Should detect two targets and next stage."""
    assert wizard.SetupProgress.has_targets
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_targets") + 1


def test_has_builds_without_enough(
    admin_user, primary_build, builder_account, project, primary_target, secondary_target
):
    """Should require at least two builds."""
    assert not wizard.SetupProgress.has_builds
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_builds")


def test_has_builds_without_enough_targets(
    admin_user, builder_account, primary_build, primary_target, project, secondary_target
):
    """Should require at least two builds from different targets."""
    mommy.make("builds.Build", target=primary_target)
    assert not wizard.SetupProgress.has_builds
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index("has_builds")


def test_has_builds(admin_user, builder_account, primary_build, primary_target, project, secondary_target):
    """Should require at least two builds from different targets."""
    mommy.make("builds.Build", target=secondary_target)
    assert wizard.SetupProgress.has_builds
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index(
        "has_working_installation"
    )


@mock.patch.multiple(
    wizard.SetupProgress, has_administrator=True, has_builds=True, has_builder=True, has_project=True, has_targets=True
)
def test_has_working_installation():
    """Should require at least two builds from different targets."""
    assert wizard.SetupProgress.has_working_installation
    assert wizard.SetupProgress.get_current_stage_index() == wizard.SetupProgress.STAGES.index(
        "has_working_installation"
    )
