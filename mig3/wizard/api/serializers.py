from rest_framework import serializers

from api.serializers import ReadOnlySerializer


class RequirementSerializer(ReadOnlySerializer):
    """API representation of installation setup requirement."""

    condition_name = serializers.CharField()
    is_satisfied = serializers.BooleanField(source="check")


class InstallationSetupSerializer(ReadOnlySerializer):
    """API representation of installation setup progress."""

    requirements = RequirementSerializer(source="REQUIREMENTS", many=True)
    current_requirement_index = serializers.IntegerField(source="get_current_requirement_index", allow_null=True)
    satisfied_requirements_percentage = serializers.IntegerField(source="calculate_satisfied_requirements_percentage")
    is_complete = serializers.BooleanField()
