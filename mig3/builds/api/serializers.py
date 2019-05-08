from hashid_field import rest as hashid_field
from rest_framework import serializers, status
from rest_framework.exceptions import APIException, MethodNotAllowed

from accounts.api import serializers as account_serializers
from api.serializers import ReadOnlySerializer
from projects import models as projects
from projects.api import serializers as project_serializers
from .. import models as builds


class Duplicate(APIException):
    """The build has already been accepted and is now immutable."""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The build has already been accepted and is now immutable."
    default_code = "duplicate"


class Regression(APIException):
    """The build introduced a regression to your migration and is unacceptable."""

    status_code = status.HTTP_409_CONFLICT
    default_detail = "The build introduced a regression to your migration and is unacceptable."
    default_code = "regression"


class CurrentBuilderAccount(object):
    """Use the BuilderAccount value from the current request's details."""

    def set_context(self, serializer_field):
        """Initialize value for callers."""
        self._builder_account = serializer_field.context["request"].auth

    def __call__(self):
        """Produce value for callers."""
        return self._builder_account


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


class ModuleTestOutcomeListSerializer(serializers.ListSerializer):
    """API representation of test results grouped by module."""

    def to_representation(self, data):
        """Filter queryset by root serializer Build instance and parent serializer Module instance."""
        module_outcomes = self.root.instance.testoutcome_set.filter(test__module=data)
        return super().to_representation(module_outcomes)


class TestOutcomeReadSerializer(ReadOnlySerializer):
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


class ModuleSerializer(ReadOnlySerializer):
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
    version = project_serializers.VersionWriteSerializer()
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
        except builds.Duplicate:
            raise Duplicate()

    def update(self, instance, validated_data):
        """Invalid operation."""
        raise MethodNotAllowed("update")


class BuildSummarySerializer(ReadOnlySerializer, serializers.ModelSerializer):
    """Summary API representation for CI builds."""

    id = hashid_field.HashidSerializerCharField(source_field="builds.Build.id")
    url = serializers.HyperlinkedIdentityField(view_name="api:build_detail", lookup_url_kwarg="build_id")
    number = serializers.CharField()
    target = serializers.PrimaryKeyRelatedField(
        queryset=projects.Target.objects.all(),
        pk_field=hashid_field.HashidSerializerCharField(source_field="projects.Target.id"),
    )
    version = project_serializers.VersionReadSerializer()
    builder = account_serializers.BuilderAccountSerializer()

    class Meta:  # noqa: D106
        model = builds.Build
        fields = ("id", "url", "target", "number", "version", "builder")


class BuildReadSerializer(BuildSummarySerializer):
    """API representation for CI builds."""

    target = project_serializers.TargetSummarySerializer()
    version = project_serializers.VersionReadSerializer()
    builder = account_serializers.BuilderAccountSerializer()
    modules = ModuleSerializer(many=True)

    class Meta(BuildSummarySerializer.Meta):  # noqa: D106
        fields = BuildSummarySerializer.Meta.fields + ("modules",)
