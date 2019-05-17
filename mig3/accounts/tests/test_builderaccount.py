from builds import models as builds
from projects import models as projects


def test_builder_statistics(another_version, builder_account, primary_build):
    """Should contain accurately aggregated statistics about the builder's relationships."""
    statistics = builder_account.statistics
    assert statistics.build_count == builds.Build.objects.filter(builder=builder_account).count()
    assert statistics.version_count == projects.Version.objects.filter(build__builder=builder_account).count()

    another_target = primary_build.target.project.target_set.create(name="Another Test Target")
    # Reset ID for new record, then assign new number, and version to remove uniqueness constraints
    primary_build.id = None
    primary_build.number = "2"
    primary_build.version = another_version
    primary_build.target = another_target
    primary_build.save()

    statistics = builder_account.statistics
    assert statistics.build_count == builds.Build.objects.filter(builder=builder_account).count()
    assert statistics.version_count == projects.Version.objects.filter(build__builder=builder_account).count()
