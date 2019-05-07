from hashid_field import rest as hashid_field
from rest_framework import serializers

from .. import models as projects


class TargetSerializer(serializers.ModelSerializer):
    """API representation for configuration targets."""

    id = hashid_field.HashidSerializerCharField(source_field="projects.Target.id")

    class Meta:  # noqa: D106
        model = projects.Target
        fields = [
            "id",
            "name",
            "python_major_version",
            "python_minor_version",
            "python_patch_version",
            "additional_details",
            "full_version",
            "python_version",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    """API representation for Projects."""

    id = hashid_field.HashidSerializerCharField(source_field="projects.Target.id")
    targets = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=projects.Target.objects.all(),
        source="target_set",
        view_name="api:target_detail",
        lookup_field="pk",
    )

    class Meta:  # noqa: D106
        model = projects.Project
        fields = ["id", "name", "repo_url", "targets"]
