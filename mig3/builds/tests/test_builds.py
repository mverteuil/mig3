from django.db import IntegrityError

import pytest

from .. import models as builds


def test_manager_create(primary_target, version, builder_account, test_results):
    """Should create build with results."""
    builds.Build.objects.create_build("1", primary_target, version, builder_account, test_results)


def test_manager_create_with_noop(primary_target, version, another_version, builder_account, test_results):
    """Should allow changes which do not move the results in a positive or negative direction."""
    builds.Build.objects.create_build("1", primary_target, version, builder_account, test_results)
    builds.Build.objects.create_build("2", primary_target, another_version, builder_account, test_results)


def test_manager_create_with_regression(
    primary_target, version, another_version, builder_account, test_results, worse_test_results
):
    """Should identify regression."""
    builds.Build.objects.create_build("1", primary_target, version, builder_account, test_results)
    with pytest.raises(builds.RegressionDetected):
        builds.Build.objects.create_build("2", primary_target, another_version, builder_account, worse_test_results)


def test_manager_create_with_progression(
    primary_target, version, another_version, builder_account, test_results, better_test_results
):
    """Should accept build with improved test results."""
    builds.Build.objects.create_build("1", primary_target, version, builder_account, test_results)
    builds.Build.objects.create_build("2", primary_target, another_version, builder_account, better_test_results)


def test_unique_for_version_and_target(primary_target, version, builder_account, test_results):
    """Should refuse multiple builds for the same target and version."""
    builds.Build.objects.create_build("1", primary_target, version, builder_account, test_results)
    with pytest.raises(IntegrityError):
        builds.Build.objects.create_build("2", primary_target, version, builder_account, test_results)


def test_unique_for_number_and_target(primary_target, version, another_version, builder_account, test_results):
    """Should refuse multiple builds for the same target and version."""
    builds.Build.objects.create_build("1", primary_target, version, builder_account, test_results)
    with pytest.raises(IntegrityError):
        builds.Build.objects.create_build("1", primary_target, another_version, builder_account, test_results)


def test_modules(primary_build):
    """Should produce the equivalent modules to the project's module_set."""
    assert primary_build.modules is not None
    assert set(primary_build.modules) == set(primary_build.target.project.module_set.all())


@pytest.mark.parametrize("result", builds.TestResult)
def test_outcome_summary(primary_build, result):
    """Should produce outcome summary with accurate result counts."""
    assert primary_build.outcome_summary is not None
    expected_outcome_count = getattr(primary_build.outcome_summary, result.name.lower())
    actual_outcome_count = builds.TestOutcome.objects.filter(result=result).count()
    assert actual_outcome_count == expected_outcome_count
