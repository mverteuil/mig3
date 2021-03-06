from unittest import mock

import projects.api.serializers.common
from projects.api import serializers


def test_project_summary_serializer(project):
    """Should produce summary serialized Project on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = projects.api.serializers.common.ProjectSummarySerializer(instance=project, context=context)
    assert serializer.data is not None


def test_project_serializer(project):
    """Should produce serialized Project on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = serializers.ProjectSerializer(instance=project, context=context)
    assert serializer.data is not None


def test_target_summary_serializer(primary_target):
    """Should produce summary serialized Target on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = projects.api.serializers.common.TargetSummarySerializer(instance=primary_target, context=context)
    assert serializer.data is not None


def test_target_serializer(primary_target):
    """Should produce serialized Target on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = serializers.TargetSerializer(instance=primary_target, context=context)
    assert serializer.data is not None


def test_version_read_serializer(version):
    """Should produce summary serialized Version on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = serializers.VersionReadSerializer(instance=version, context=context)
    assert serializer.data is not None


def test_version_write_serializer(db):
    """Should produce Build with incoming serialized version request data."""
    data = {"hash": "a2" * 20, "author": "user@example.com"}
    serializer = projects.api.serializers.common.VersionWriteSerializer(data=data)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.save()
