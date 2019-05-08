from unittest import mock

import pytest
from rest_framework.exceptions import MethodNotAllowed

from ..api import serializers


def test_current_builder_account(db):
    """Should return request authenticated BuilderAccount."""
    expected_value = mock.Mock(name="BuilderAccount")
    request = mock.Mock(name="request", auth=expected_value)
    field = mock.Mock(name="serializer_field", context={"request": request})
    value_builder = serializers.CurrentBuilderAccount()
    value_builder.set_context(field)
    assert value_builder() == expected_value


def test_build_summary_serializer(build):
    """Should produce summary serialized Build on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = serializers.BuildSummarySerializer(instance=build, context=context)
    assert serializer.data is not None


def test_build_read_serializer(build):
    """Should produce serialized Build on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = serializers.BuildReadSerializer(instance=build, context=context)
    assert serializer.data is not None


def test_build_write_serializer_create(django_db_reset_sequences, serialized_build, builder_account, target):
    """Should produce Build with incoming serialized build request data."""
    context = {"request": mock.Mock(name="request", auth=builder_account)}
    serializer = serializers.BuildWriteSerializer(data=serialized_build, context=context)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.save()


def test_build_write_serializer_create_with_duplicate(
    build, serialized_build, builder_account, target, django_db_reset_sequences
):
    """Should refuse duplicate builds."""
    assert build.number == serialized_build["number"]
    context = {"request": mock.Mock(name="request", auth=builder_account)}
    serializer = serializers.BuildWriteSerializer(data=serialized_build, context=context)
    assert serializer.is_valid(raise_exception=True)
    with pytest.raises(serializers.Duplicate):
        serializer.save()


def test_build_write_serializer_create_with_regression(
    django_db_reset_sequences, serialized_build, serialized_build_regression, builder_account, target
):
    """Should refuse to create regressive builds."""
    context = {"request": mock.Mock(name="request", auth=builder_account)}
    valid_serializer = serializers.BuildWriteSerializer(data=serialized_build, context=context)
    assert valid_serializer.is_valid()
    valid_serializer.save()

    regression_serializer = serializers.BuildWriteSerializer(data=serialized_build_regression, context=context)
    assert regression_serializer.is_valid()
    with pytest.raises(serializers.Regression):
        assert regression_serializer.save()


def test_build_write_serializer_update(django_db_reset_sequences, build, serialized_build, builder_account, target):
    """Should refuse update operations on Builds."""
    context = {"request": mock.Mock(name="request", auth=builder_account)}
    serializer = serializers.BuildWriteSerializer(data=serialized_build, instance=build, context=context)
    assert serializer.is_valid()
    with pytest.raises(MethodNotAllowed):
        serializer.save()
