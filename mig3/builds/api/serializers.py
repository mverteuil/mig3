import logging

from django.conf import settings
from django.contrib.auth import get_user_model

from hashid_field import rest as hashid_field
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from accounts.api import serializers as account_serializers
from projects import models as projects
from projects.api import serializers as project_serializers
from .. import models as builds

logger = logging.getLogger(__name__)


class Regression(APIException):
    """The build introduced a regression to your migration and is unacceptable."""

    status_code = status.HTTP_409_CONFLICT
    default_detail = "The build introduced a regression to your migration and is unacceptable."
    default_code = "conflict"


class CurrentBuilderAccount(object):
    """Use the BuilderAccount value from the current request's details."""

    def set_context(self, serializer_field):
        """Initialize value for callers."""
        self.builder_account = serializer_field.context["request"].auth

    def __call__(self):
        """Produce value for callers."""
        return self.builder_account


class TestResultField(serializers.Field):
    """Serialize TestOutcome.Result values."""

    def get_attribute(self, instance):
        """Return the object to deserialize."""
        if self.source_attrs:
            return super().get_attribute(instance)
        else:
            return instance

    def to_internal_value(self, data: str):
        """Deserialize result for storage."""
        return builds.TestOutcome.Results[data.upper()]

    def to_representation(self, value: int):
        """Convert integer value to result label."""
        return builds.TestOutcome.Results(value).name


class VersionField(serializers.Field):
    """Consume version author details for a Build submitted through the API.

    Will create a new inactive UserAccount for the author if the email has not been seen before.
    """

    def _get_or_create_author(self, email: str) -> settings.AUTH_USER_MODEL:
        UserAccount = get_user_model()
        try:
            return UserAccount.objects.get_by_natural_key(email)
        except UserAccount.DoesNotExist:
            return UserAccount.objects.create_user(email=email)

    def to_internal_value(self, data: dict) -> projects.Version:
        """Deserialize version and author for storage."""
        return projects.Version.objects.create(hash=data["hash"], author=self._get_or_create_author(data["author"]))

    def to_representation(self, value) -> str:
        """Serialize version for representation."""
        return str(value)


class ModuleTestOutcomeListSerializer(serializers.ListSerializer):
    """API representation of test results grouped by module."""

    def to_representation(self, data):
        """Filter queryset by root serializer Build instance and parent serializer Module instance."""
        module_outcomes = self.root.instance.testoutcome_set.filter(test__module=data)
        return super().to_representation(module_outcomes)


class TestOutcomeReadSerializer(serializers.Serializer):
    """API representation for test results."""

    name = serializers.CharField(source="test.name")
    result = TestResultField()

    class Meta:  # noqa: D106
        list_serializer_class = ModuleTestOutcomeListSerializer


class TestOutcomeWriteSerializer(serializers.Serializer):
    """Consume TestOutcomes submitted through the API."""

    module = serializers.CharField()
    test = serializers.CharField()
    result = TestResultField()


class ModuleOutcomeSerializer(serializers.Serializer):
    """API representation for python test modules."""

    path = serializers.CharField()
    tests = TestOutcomeReadSerializer(many=True, source="*")


class BuildWriteSerializer(serializers.Serializer):
    """Consume Builds submitted through the API."""

    target = serializers.PrimaryKeyRelatedField(
        queryset=projects.Target.objects.all(),
        pk_field=hashid_field.HashidSerializerCharField(source_field="projects.Target.id"),
    )
    number = serializers.CharField()
    version = VersionField()
    builder = serializers.HiddenField(default=CurrentBuilderAccount())
    results = TestOutcomeWriteSerializer(many=True, write_only=True)

    class Meta:  # noqa: D106
        model = builds.Build

    def create(self, validated_data: dict) -> builds.Build:
        """Create a new Build from API request."""
        try:
            return builds.Build.objects.create_build(**validated_data)
        except builds.RegressionDetected as e:
            raise Regression(str(e))


class BuildSummarySerializer(serializers.ModelSerializer):
    """Summary API representation for CI builds."""

    id = hashid_field.HashidSerializerCharField(source_field="builds.Build.id")
    url = serializers.HyperlinkedIdentityField(view_name="api:build_detail", lookup_url_kwarg="build_id")
    number = serializers.CharField()
    target = serializers.PrimaryKeyRelatedField(
        queryset=projects.Target.objects.all(),
        pk_field=hashid_field.HashidSerializerCharField(source_field="projects.Target.id"),
    )
    version = VersionField()
    builder = account_serializers.BuilderAccountSerializer()

    class Meta:  # noqa: D106
        model = builds.Build
        fields = ("id", "url", "target", "number", "version", "builder")


class BuildReadSerializer(BuildSummarySerializer):
    """API representation for CI builds."""

    target = project_serializers.TargetSummarySerializer()
    version = project_serializers.VersionSerializer()
    builder = account_serializers.BuilderAccountSerializer()
    modules = ModuleOutcomeSerializer(many=True)

    class Meta(BuildSummarySerializer.Meta):  # noqa: D106
        fields = BuildSummarySerializer.Meta.fields + ("modules",)
