import logging

from rest_framework import serializers

from builds import models as builds
from projects import models as projects

logger = logging.getLogger(__name__)


class VersionSerializer(serializers.ModelSerializer):
    hash = serializers.CharField(source="id")

    class Meta:
        model = projects.Version
        fields = ("hash", "author")


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
        logger.debug(tests)
        build = builds.Build.objects.create(**validated_data)
        return build

    def save(self, **kwargs):
        return super().save(**kwargs)
