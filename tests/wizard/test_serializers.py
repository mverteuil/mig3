import pytest

from wizard import models as wizard
from wizard.api import serializers


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


def test_initial_builder(builder_account, db, admin_request):
    """Should return initial builder."""
    serializer = serializers.InstallationSetupSerializer(
        instance=wizard.InstallationSetup, context={"request": admin_request}
    )
    serialized_data = serializer.data
    assert serialized_data["initial_builder"]["id"] == builder_account.id


def test_initial_builder_with_non_admin_request(builder_account, db, non_admin_request):
    """Should continue to enforce admin requirement from BuilderAccountSerializer."""
    serializer = serializers.InstallationSetupSerializer(
        instance=wizard.InstallationSetup, context={"request": non_admin_request}
    )
    with pytest.raises(ValueError, match="Context request with administrator required"):
        assert serializer.data is None


def test_initial_builder_not_present(admin_request, db):
    """Should return none when builder is not present."""
    serializer = serializers.InstallationSetupSerializer(
        instance=wizard.InstallationSetup, context={"request": admin_request}
    )
    serialized_data = serializer.data
    assert serialized_data["initial_builder"] is None


def test_initial_project(admin_request, db, project):
    """Should return initial project."""
    serializer = serializers.InstallationSetupSerializer(
        instance=wizard.InstallationSetup, context={"request": admin_request}
    )
    serialized_data = serializer.data
    assert serialized_data["initial_project"]["id"] == project.id


def test_initial_project_not_present(admin_request, db):
    """Should return none if project is not present."""
    serializer = serializers.InstallationSetupSerializer(
        instance=wizard.InstallationSetup, context={"request": admin_request}
    )
    serialized_data = serializer.data
    assert serialized_data["initial_project"] is None
