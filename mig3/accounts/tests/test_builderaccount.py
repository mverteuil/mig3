from model_mommy import mommy

from builds import models as builds
from projects import models as projects


def test_builder_statistics(another_version, builder_account, project, primary_build):
    """Should contain accurately aggregated statistics about the builder's relationships."""
    statistics = builder_account.statistics
    assert statistics.build_count == builds.Build.objects.filter(builder=builder_account).count()
    assert statistics.version_count == projects.Version.objects.filter(build__builder=builder_account).count()

    mommy.make("builds.Build", number="2", target__project=project)

    statistics = builder_account.statistics
    assert statistics.build_count == builds.Build.objects.filter(builder=builder_account).count()
    assert statistics.version_count == projects.Version.objects.filter(build__builder=builder_account).count()
