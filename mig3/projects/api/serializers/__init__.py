from builds.api.serializers import common as build_common_serializers
from .common import ProjectSummarySerializer, TargetSummarySerializer, TargetWriteSerializer, VersionReadSerializer

__all__ = (
    "ProjectSerializer",
    "ProjectSummarySerializer",
    "TargetSerializer",
    "TargetSummarySerializer",
    "TargetWriteSerializer",
    "VersionReadSerializer",
)


class TargetSerializer(TargetSummarySerializer):
    """API representation for configuration targets."""

    project = ProjectSummarySerializer()
    builds = build_common_serializers.BuildSummarySerializer(many=True, source="build_set")

    class Meta(TargetSummarySerializer.Meta):  # noqa: D106
        fields = TargetSummarySerializer.Meta.fields + ("builds", "project")


class ProjectSerializer(ProjectSummarySerializer):
    """API representation for Projects."""

    targets = TargetSummarySerializer(many=True, source="target_set", read_only=True)

    class Meta(ProjectSummarySerializer.Meta):  # noqa: D106
        fields = ProjectSummarySerializer.Meta.fields + ("targets",)


class ExtendedProjectSerializer(ProjectSerializer):
    """API representation for Projects will full Target details."""

    targets = TargetSerializer(many=True, source="target_set", read_only=True)
