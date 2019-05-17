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


def test_build_summary_serializer(primary_build):
    """Should produce summary serialized Build on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = serializers.BuildSummarySerializer(instance=primary_build, context=context)
    assert serializer.data is not None


def test_build_read_serializer(primary_build):
    """Should produce serialized Build on the happy path."""
    context = {"request": mock.Mock(name="request", GET={})}
    serializer = serializers.BuildReadSerializer(instance=primary_build, context=context)
    assert serializer.data is not None


def test_build_write_serializer_create(builder_account, django_db_reset_sequences, serialized_build, primary_target):
    """Should produce Build with incoming serialized build request data."""
    context = {"request": mock.Mock(name="request", auth=builder_account)}
    serializer = serializers.BuildWriteSerializer(data=serialized_build, context=context)
    assert serializer.is_valid(raise_exception=True)
    assert serializer.save()


def test_build_write_serializer_create_with_duplicate(
    primary_build, builder_account, django_db_reset_sequences, serialized_build, primary_target
):
    """Should refuse duplicate builds."""
    assert primary_build.number == serialized_build["number"]
    context = {"request": mock.Mock(name="request", auth=builder_account)}
    serializer = serializers.BuildWriteSerializer(data=serialized_build, context=context)
    assert serializer.is_valid(raise_exception=True)
    with pytest.raises(serializers.Duplicate):
        serializer.save()


def test_build_write_serializer_create_with_regression(
    builder_account, django_db_reset_sequences, serialized_build, serialized_build_regression, primary_target
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


def test_build_write_serializer_update(
    primary_build, builder_account, django_db_reset_sequences, serialized_build, primary_target
):
    """Should refuse update operations on Builds."""
    context = {"request": mock.Mock(name="request", auth=builder_account)}
    serializer = serializers.BuildWriteSerializer(data=serialized_build, instance=primary_build, context=context)
    assert serializer.is_valid()
    with pytest.raises(MethodNotAllowed):
        serializer.save()
