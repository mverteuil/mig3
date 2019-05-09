from hashid_field import rest as hashid_field
from rest_framework import serializers

from accounts.api import serializers as account_serializers
from api.serializers import ReadOnlySerializer
from builds import models as builds
from projects import models as projects
from projects.api.serializers import common as projects_common_serializers


class BuildSummarySerializer(ReadOnlySerializer, serializers.ModelSerializer):
    """Summary API representation for CI builds."""

    id = hashid_field.HashidSerializerCharField(source_field="builds.Build.id")
    url = serializers.HyperlinkedIdentityField(view_name="api:build_detail", lookup_url_kwarg="build_id")
    number = serializers.CharField()
    target = serializers.PrimaryKeyRelatedField(
        queryset=projects.Target.objects.all(),
        pk_field=hashid_field.HashidSerializerCharField(source_field="projects.Target.id"),
    )
    version = projects_common_serializers.VersionReadSerializer()
    builder = account_serializers.BuilderAccountSerializer()

    class Meta:  # noqa: D106
        model = builds.Build
        fields = ("id", "url", "target", "number", "version", "builder")
