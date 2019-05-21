from hashid_field import rest as hashid_field
from rest_framework import serializers

from accounts.api import serializers as accounts_serializers
from api.serializers import ReadOnlySerializer
from projects import models as projects


class VersionReadSerializer(serializers.ModelSerializer):
    """API representation for repository majorAndMinorVersions."""

    author = accounts_serializers.UserAccountSerializer()

    class Meta:  # noqa: D106
        model = projects.Version
        fields = ("hash", "author")


class ProjectStatisticsSerializer(ReadOnlySerializer):
    """Summary API representation for project relationship counts."""

    target_count = serializers.IntegerField()
    module_count = serializers.IntegerField()
    test_count = serializers.IntegerField()


class ProjectSummarySerializer(serializers.ModelSerializer):
    """Summary API representation for projects."""

    id = hashid_field.HashidSerializerCharField(source_field="projects.Target.id", read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="api:project_detail", lookup_url_kwarg="project_id")
    statistics = ProjectStatisticsSerializer(read_only=True)

    class Meta:  # noqa: D106
        model = projects.Project
        fields = ("id", "name", "url", "repo_url", "statistics")


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


class VersionWriteSerializer(serializers.ModelSerializer):
    """Consume version author details for a Build submitted through the API.

    Will create a new inactive UserAccount for the author if the email has not been seen before.
    """

    hash = serializers.CharField()
    author = accounts_serializers.UserAccountField()

    class Meta:  # noqa: D106
        model = projects.Version
        fields = ("hash", "author")
