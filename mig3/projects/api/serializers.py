from hashid_field import rest as hashid_field
from rest_framework import serializers

from accounts.api import serializers as accounts_serializers
from builds import models as builds
from .. import models as projects


class VersionSerializer(serializers.ModelSerializer):
    """API representation for repository versions."""

    author = accounts_serializers.UserAccountSerializer()

    class Meta:  # noqa: D106
        model = projects.Version
        fields = ("hash", "author")


class TargetSummarySerializer(serializers.ModelSerializer):
    """Summary API representation for configuration targets."""

    id = hashid_field.HashidSerializerCharField(source_field="projects.Target.id")
    url = serializers.HyperlinkedIdentityField(view_name="api:target_detail", lookup_url_kwarg="target_id")

    class Meta:  # noqa: D106
        model = projects.Target
        fields = (
            "id",
            "url",
            "name",
            "python_major_version",
            "python_minor_version",
            "python_patch_version",
            "additional_details",
            "full_version",
            "python_version",
        )


class TargetSerializer(TargetSummarySerializer):
    """API representation for configuration targets."""

    builds = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=builds.Build.objects.all(),
        source="build_set",
        view_name="api:build_detail",
        lookup_field="pk",
    )

    class Meta(TargetSummarySerializer.Meta):  # noqa: D106
        fields = TargetSummarySerializer.Meta.fields + ("builds",)


class ProjectSummarySerializer(serializers.ModelSerializer):
    """Summary API representation for Projects."""

    id = hashid_field.HashidSerializerCharField(source_field="projects.Target.id")
    url = serializers.HyperlinkedIdentityField(view_name="api:project_detail", lookup_url_kwarg="project_id")

    class Meta:  # noqa: D106
        model = projects.Project
        fields = ("id", "name", "url", "repo_url")


class ProjectSerializer(ProjectSummarySerializer):
    """API representation for Projects."""

    targets = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=projects.Target.objects.all(),
        source="target_set",
        view_name="api:target_detail",
        lookup_field="pk",
    )

    class Meta(ProjectSummarySerializer.Meta):  # noqa: D106
        fields = ProjectSummarySerializer.Meta.fields + ("targets",)
