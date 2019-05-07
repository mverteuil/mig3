import logging

from django.conf import settings
from django.contrib.auth import get_user_model

from hashid_field import rest as hashid_field
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from builds import models as builds
from projects import models as projects

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
    """Consume submitted test result for a TestOutcome."""

    def get_attribute(self, instance):
        """Return the object to deserialize."""
        return instance

    def to_internal_value(self, data):
        """Deserialize result for storage."""
        return builds.TestOutcome.Results[data.upper()]

    def to_representation(self, value):
        """Serialize result for representation."""
        return value


class VersionField(serializers.Field):
    """Consume submitted version author details for a Build.

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


class TestOutcomeSerializer(serializers.Serializer):
    """Consume TestOutcomes submitted through the API."""

    module = serializers.CharField()
    test = serializers.CharField()
    result = TestResultField()


class BuildSerializer(serializers.Serializer):
    """Consume Builds submitted through the API."""

    target = serializers.PrimaryKeyRelatedField(
        queryset=projects.Target.objects.all(),
        pk_field=hashid_field.HashidSerializerCharField(source_field="projects.Target.id"),
    )
    number = serializers.CharField()
    version = VersionField()
    builder = serializers.HiddenField(default=CurrentBuilderAccount())
    results = TestOutcomeSerializer(many=True, write_only=True)

    class Meta:  # noqa: D106
        model = builds.Build

    def create(self, validated_data: dict) -> builds.Build:
        """Create a new Build from API request."""
        try:
            return builds.Build.objects.create_build(**validated_data)
        except builds.RegressionDetected as e:
            raise Regression(str(e))
