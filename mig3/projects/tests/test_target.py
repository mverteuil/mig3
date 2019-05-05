import pytest

from projects import models as projects


@pytest.mark.parametrize(
    ["version_tuple", "additional", "expected_result"],
    [
        [(3, 6, 8), None, "3.6.8"],
        [(3, 7, 3), None, "3.7.3"],
        [(3, 7, 3), "dev", "3.7.3+dev"],
        [(3, 8, 0), "django==2.2", "3.8.0+django==2.2"],
    ],
)
def test_target_full_version(version_tuple, additional, expected_result):
    """Should generate expected full version identifier from Target state."""
    python_major, python_minor, python_patch = version_tuple
    target = projects.Target(
        python_major_version=python_major,
        python_minor_version=python_minor,
        python_patch_version=python_patch,
        additional_details=additional,
    )
    assert target.full_version == expected_result, target.full_version


@pytest.mark.parametrize(
    ["version_tuple", "expected_result"],
    [[(3, 6, 8), "3.6.8"], [(3, 7, 3), "3.7.3"], [(3, 7, 0), "3.7.0"], [(3, 8, 0), "3.8.0"]],
)
def test_target_python_version(version_tuple, expected_result):
    """Should generate expected python version identifier from Target state."""
    python_major, python_minor, python_patch = version_tuple
    target = projects.Target(
        python_major_version=python_major, python_minor_version=python_minor, python_patch_version=python_patch
    )
    assert target.python_version == expected_result, target.python_version
