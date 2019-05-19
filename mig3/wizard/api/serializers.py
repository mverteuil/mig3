from rest_framework import serializers

from api.serializers import ReadOnlySerializer
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
        _, id = obj.__name__.split("Has")
        return id


class InstallationSetupSerializer(ReadOnlySerializer):
    """API representation of installation setup progress."""

    requirements = RequirementSerializer(source="REQUIREMENTS", many=True)
    current_requirement_index = serializers.IntegerField(source="get_current_requirement_index", allow_null=True)
    satisfied_requirements_percentage = serializers.IntegerField(source="calculate_satisfied_requirements_percentage")
    is_complete = serializers.BooleanField()
