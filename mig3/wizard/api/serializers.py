from rest_framework import serializers

from accounts.api import serializers as account_serializers
from api.serializers import ReadOnlySerializer
from projects.api import serializers as project_serializers
from wizard import models as wizard


class RequirementSerializer(ReadOnlySerializer):
    """API representation of installation setup requirement."""

    id = serializers.SerializerMethodField()
    condition_name = serializers.CharField()
    is_satisfied = serializers.BooleanField(source="check")

    @staticmethod
    def get_id(obj: wizard.RequirementChecker) -> str:
        """Use the requirement checker class name, less the "Has"-prefix, as unique identifier.

        Used in the frontend to choose the correct form component for the setup wizard.
        """
        _, requirement_id = obj.__name__.split("Has")
        return requirement_id


class InstallationSetupSerializer(ReadOnlySerializer):
    """API representation of installation setup progress."""

    requirements = RequirementSerializer(source="REQUIREMENTS", many=True)
    current_requirement_index = serializers.IntegerField(source="get_current_requirement_index", allow_null=True)
    satisfied_requirements_percentage = serializers.IntegerField(source="calculate_satisfied_requirements_percentage")
    initial_builder = account_serializers.BuilderAccountSerializer(source="find_initial_builder", read_only=True)
    initial_project = project_serializers.ExtendedProjectSerializer(source="find_initial_project", read_only=True)
    is_complete = serializers.BooleanField()
