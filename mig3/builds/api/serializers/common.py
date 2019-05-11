from hashid_field import rest as hashid_field
from rest_framework import serializers

from accounts.api import serializers as account_serializers
from api.serializers import ReadOnlySerializer
from builds import models as builds
from projects.api.serializers import common as project_common_serializers


class OutcomeSummarySerializer(ReadOnlySerializer):
    """Summarize result counts for each test result type."""

    error = serializers.IntegerField()
    failed = serializers.IntegerField()
    passed = serializers.IntegerField()
    skipped = serializers.IntegerField()
    xfailed = serializers.IntegerField()


class BuildSummarySerializer(ReadOnlySerializer, serializers.ModelSerializer):
    """Summary API representation for CI builds."""

    id = hashid_field.HashidSerializerCharField(source_field="builds.Build.id")
    url = serializers.HyperlinkedIdentityField(view_name="api:build_detail", lookup_url_kwarg="build_id")
    number = serializers.CharField()
    builder = account_serializers.BuilderAccountSerializer()
    version = project_common_serializers.VersionReadSerializer()
    outcome_summary = OutcomeSummarySerializer()

    class Meta:  # noqa: D106
        model = builds.Build
        fields = ("id", "url", "number", "version", "builder", "outcome_summary")
