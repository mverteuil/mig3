from rest_framework import serializers

from projects import models as projects


class VersionSerializer(serializers.ModelSerializer):
    hash = serializers.CharField(source="id")

    class Meta:
        model = projects.Version


class BuildSerializer(serializers.Serializer):
    version = VersionSerializer()
    target = serializers.CharField()
    number = serializers.CharField()
    builder = serializers.CharField()
