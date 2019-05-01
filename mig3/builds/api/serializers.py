import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers

from builds import models as builds
from projects import models as projects

logger = logging.getLogger(__name__)


class VersionAuthorField(serializers.Field):
    def to_internal_value(self, data):
        UserAccount = get_user_model()
        author, _ = UserAccount.objects.get_or_create(email=data["author"])
        return author

    def to_representation(self, value):
        return value.email


class VersionSerializer(serializers.ModelSerializer):
    author = VersionAuthorField(required=True)
    hash = serializers.CharField(source="id")

    class Meta:
        model = projects.Version
        fields = ("hash", "author")

    def create(self, validated_data):
        return super().create(validated_data)

    def to_representation(self, instance):
        return super().to_representation(instance)

    def to_internal_value(self, data):
        return super().to_internal_value(data)


class TestSerializer(serializers.Serializer):
    module = serializers.CharField(source="module__name")


class BuildSerializer(serializers.Serializer):
    version = VersionSerializer()
    target = serializers.CharField()
    number = serializers.CharField()
    builder = serializers.SerializerMethodField()
    tests = TestSerializer(many=True)

    def get_builder(self, obj):
        return self.context["request"].auth

    def create(self, validated_data):
        tests = validated_data.pop("tests")
        version = validated_data.pop("version")
        logger.debug(tests, version)
        build = builds.Build.objects.create(**validated_data)
        return build

    def save(self, **kwargs):
        return super().save(**kwargs)
