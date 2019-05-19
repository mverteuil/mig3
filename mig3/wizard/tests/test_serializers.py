import pytest

from .. import models as wizard
from ..api import serializers


class HasAlwaysFalse(wizard.RequirementChecker):
    """Always False."""

    condition_name: str = "Always False"

    @staticmethod
    def check() -> bool:  # noqa: D102
        return False


class HasAlwaysTrue(wizard.RequirementChecker):
    """Always True."""

    condition_name: str = "Always True"

    @staticmethod
    def check() -> bool:  # noqa: D102
        return True


@pytest.mark.parametrize("requirement", [HasAlwaysFalse, HasAlwaysTrue])
def test_requirement_serializer(requirement):
    """Should accurately serialize requirement as defined."""
    serializer = serializers.RequirementSerializer(instance=requirement)
    serialized_data = serializer.data
    assert serialized_data["is_satisfied"] is requirement.check()
    assert serialized_data["condition_name"] is requirement.condition_name
    assert serialized_data["id"] == requirement.__name__.split("Has")[1]


def test_installation_setup_serializer(db):
    """Should accurately serialize installation setup state."""
    serializer = serializers.InstallationSetupSerializer(instance=wizard.InstallationSetup)
    serialized_data = serializer.data
    assert len(serialized_data["requirements"]) == len(wizard.InstallationSetup.REQUIREMENTS)
    expected_satisfied_requirements_percentage = wizard.InstallationSetup.calculate_satisfied_requirements_percentage()
    assert serialized_data["satisfied_requirements_percentage"] == expected_satisfied_requirements_percentage
    assert serialized_data["is_complete"] is False
    assert serialized_data["current_requirement_index"] == wizard.InstallationSetup.get_current_requirement_index()
