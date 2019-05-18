import inspect
from unittest import mock

import pytest
from model_mommy import mommy

from . import models as wizard


def get_requirement_index(requirement):
    """Find the index in InstallationRequirements.REQUIREMENTS for a concrete RequirementChecker implementation."""
    return wizard.InstallationSetup.REQUIREMENTS.index(requirement)


def test_no_progress(db):
    """All stages should be negative at the beginning."""
    for module_member in inspect.getmembers(wizard):
        if inspect.isclass(module_member) and issubclass(module_member, wizard.RequirementChecker):
            assert module_member.check() is False


def test_has_administrator(admin_user):
    """Should detect administrator and next stage."""
    assert wizard.HasAdministrator.check()
    expected_index = get_requirement_index(wizard.HasAdministrator) + 1
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_builder(admin_user, builder_account):
    """Should detect builder and next stage."""
    assert wizard.HasBuilder.check()
    expected_index = get_requirement_index(wizard.HasBuilder) + 1
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_project(admin_user, builder_account, project):
    """Should detect builder and next stage."""
    assert wizard.HasProject.check()
    expected_index = get_requirement_index(wizard.HasProject) + 1
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_targets_without_enough(admin_user, builder_account, primary_target, project):
    """Should require two project targets."""
    assert not wizard.HasTargets.check()
    expected_index = get_requirement_index(wizard.HasTargets)
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_targets_without_enough_for_same_project(admin_user, builder_account, primary_target, project):
    """Should require two targets attached to the same project."""
    mommy.make("projects.Target")
    assert not wizard.HasTargets.check()
    expected_index = get_requirement_index(wizard.HasTargets)
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_targets(admin_user, builder_account, primary_target, project, secondary_target):
    """Should detect two targets and next stage."""
    assert wizard.HasTargets.check()
    expected_index = get_requirement_index(wizard.HasTargets) + 1
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_builds_without_enough(
    admin_user, primary_build, builder_account, project, primary_target, secondary_target
):
    """Should require at least two builds."""
    assert not wizard.HasBuilds.check()
    expected_index = get_requirement_index(wizard.HasBuilds)
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_builds_without_enough_targets(
    admin_user, builder_account, primary_build, primary_target, project, secondary_target
):
    """Should require at least two builds from different targets."""
    mommy.make("builds.Build", target=primary_target)
    assert not wizard.HasBuilds.check()
    expected_index = get_requirement_index(wizard.HasBuilds)
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_has_builds(admin_user, builder_account, primary_build, primary_target, project, secondary_target):
    """Should require at least two builds from different targets."""
    mommy.make("builds.Build", target=secondary_target)
    assert wizard.HasBuilds.check()
    expected_index = None  # Because this is the last requirement
    assert wizard.InstallationSetup.get_current_requirement_index() == expected_index


def test_is_complete():
    """Should require all defined requirements to be met."""
    mock_requirements = [mock.Mock(name="requirement") for _ in range(3)]
    with mock.patch.object(wizard.InstallationSetup, "REQUIREMENTS", mock_requirements):
        assert wizard.InstallationSetup.is_complete()

    for requirement in mock_requirements:
        requirement.check.assert_called_once()


def test_final_index():
    """Should produce None when all requirements have been met."""
    mock_requirements = [mock.Mock(name="requirement") for _ in range(3)]
    with mock.patch.object(wizard.InstallationSetup, "REQUIREMENTS", mock_requirements):
        assert wizard.InstallationSetup.get_current_requirement_index() is None

    for requirement in mock_requirements:
        requirement.check.assert_called_once()


@pytest.mark.parametrize(
    ("satisfied_count", "unsatisfied_count", "expected_result"),
    [(0, 1, 0), (1, 0, 100), (1, 2, 33), (2, 3, 40), (17, 28, 37)],
)
def test_satisfied_requirements_percentage(satisfied_count, unsatisfied_count, expected_result):
    """Should calculate correct percentage, and round the result in deterministic way."""
    satisfied_requirements = [mock.Mock(**{"check.return_value": True})] * satisfied_count
    unsatisfied_requirements = [mock.Mock(**{"check.return_value": False})] * unsatisfied_count
    mock_requirements = satisfied_requirements + unsatisfied_requirements
    with mock.patch.object(wizard.InstallationSetup, "REQUIREMENTS", mock_requirements):
        assert wizard.InstallationSetup.calculate_satisfied_requirements_percentage() == expected_result
