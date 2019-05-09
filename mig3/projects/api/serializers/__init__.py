from builds.api.serializers import common as builds_common_serializers
from .common import ProjectSummarySerializer, TargetSummarySerializer, VersionReadSerializer

__all__ = (
    "ProjectSerializer",
    "ProjectSummarySerializer",
    "TargetSerializer",
    "TargetSummarySerializer",
    "VersionReadSerializer",
)


class TargetSerializer(TargetSummarySerializer):
    """API representation for configuration targets."""

    project = ProjectSummarySerializer()
    builds = builds_common_serializers.BuildSummarySerializer(many=True, source="build_set")

    class Meta(TargetSummarySerializer.Meta):  # noqa: D106
        fields = TargetSummarySerializer.Meta.fields + ("builds", "project")


class ProjectSerializer(ProjectSummarySerializer):
    """API representation for Projects."""

    targets = TargetSummarySerializer(many=True, source="target_set")

    class Meta(ProjectSummarySerializer.Meta):  # noqa: D106
        fields = ProjectSummarySerializer.Meta.fields + ("targets",)
