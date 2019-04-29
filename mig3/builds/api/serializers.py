from rest_framework import serializers

from projects import models as projects


class VersionSerializer(serializers.ModelSerializer):
    hash = serializers.CharField(source="id")

    class Meta:
        model = projects.Version
        fields = ("hash", "owner")


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
