import logging

from django.contrib.auth import get_user_model
from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers

from builds import models as builds
from projects import models as projects

logger = logging.getLogger(__name__)


class CurrentBuilderAccount(object):
    def set_context(self, serializer_field):
        self.builder_account = serializer_field.context["request"].auth

    def __call__(self):
        return self.builder_account


class TestResultField(serializers.Field):
    def get_attribute(self, instance):
        return instance

    def to_internal_value(self, data):
        return builds.TestOutcome.Results[data.upper()]

    def to_representation(self, value):
        return value


class VersionField(serializers.Field):
    def _get_or_create_author(self, email):
        UserAccount = get_user_model()
        try:
            author = UserAccount.objects.get_by_natural_key(email)
        except UserAccount.DoesNotExist:
            author = UserAccount.objects.create_user(email=email)
        finally:
            return author

    def to_internal_value(self, data):
        return projects.Version.objects.create(hash=data["hash"], author=self._get_or_create_author(data["author"]))

    def to_representation(self, value):
        return str(value)


class TestOutcomeSerializer(serializers.Serializer):
    module = serializers.CharField(source="test__module__name")
    test = serializers.CharField(source="test__name")
    outcome = TestResultField(source="result")


class BuildSerializer(serializers.Serializer):
    number = serializers.CharField()
    builder = serializers.HiddenField(default=CurrentBuilderAccount())
    tests = TestOutcomeSerializer(many=True, write_only=True)
    target = serializers.PrimaryKeyRelatedField(
        queryset=projects.Target.objects.all(), pk_field=HashidSerializerCharField(source_field="projects.Target.id")
    )
    version = VersionField()

    def create(self, validated_data):
        tests = validated_data.pop("tests")
        logger.debug(tests)
        build = builds.Build.objects.create(**validated_data)
        return build

    def save(self, **kwargs):
        return super().save(**kwargs)
