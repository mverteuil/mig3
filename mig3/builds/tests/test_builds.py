import pytest

from builds import models as builds


def test_manager_create(target, version, builder_account, test_results):
    """Should create build with results."""
    builds.Build.objects.create_build("0", target, version, builder_account, test_results)


def test_manager_create_with_noop(target, version, builder_account, test_results):
    """Should allow changes which do not move the results in a positive or negative direction."""
    builds.Build.objects.create_build("0", target, version, builder_account, test_results)
    builds.Build.objects.create_build("1", target, version, builder_account, test_results)


def test_manager_create_with_regression(target, version, builder_account, test_results, worse_test_results):
    """Should identify regression."""
    builds.Build.objects.create_build("0", target, version, builder_account, test_results)
    with pytest.raises(builds.RegressionDetected):
        builds.Build.objects.create_build("1", target, version, builder_account, worse_test_results)


def test_manager_create_with_progression(target, version, builder_account, test_results, better_test_results):
    """Should accept build with improved test results."""
    builds.Build.objects.create_build("0", target, version, builder_account, test_results)
    builds.Build.objects.create_build("1", target, version, builder_account, better_test_results)
