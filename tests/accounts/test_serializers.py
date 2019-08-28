from django.contrib.auth import get_user_model

import pytest

from accounts.api import serializers


def test_user_account_field_read():
    """Should generate string representation of given UserAccount."""
    user_account = get_user_model()(email="user@example.com", name="Test User")
    actual = serializers.UserAccountField().to_representation(user_account)
    assert actual == str(user_account)


def test_user_account_field_write_new(db):
    """Should create UserAccounts that don't already exist."""
    expected = "user@example.com"
    assert not get_user_model().objects.filter(email=expected).exists()
    user_account = serializers.UserAccountField().to_internal_value(expected)
    assert user_account.email == expected


def test_user_account_field_write_existing(user_account):
    """Should find existing UserAccounts."""
    actual = serializers.UserAccountField().to_internal_value(user_account.email)
    assert actual == user_account


def test_builder_account_serializer(admin_request, builder_account):
    """Should produce serialized BuilderAccount on the happy path."""
    serializer = serializers.BuilderAccountSerializer(instance=builder_account, context={"request": admin_request})
    assert serializer.data is not None
    assert "token" in serializer.data


def test_builder_account_serializer_without_admin(non_admin_request, builder_account):
    """Should explode if created with regular user request."""
    serializer = serializers.BuilderAccountSerializer(instance=builder_account, context={"request": non_admin_request})
    with pytest.raises(ValueError):
        assert serializer.data is None


def test_builder_account_serializer_without_context_request(builder_account):
    """Should explode if created without context request."""
    serializer = serializers.BuilderAccountSerializer(instance=builder_account, context={})
    with pytest.raises(ValueError):
        assert serializer.data is None


def test_builder_account_serializer_without_context(builder_account):
    """Should explode if created without context."""
    serializer = serializers.BuilderAccountSerializer(instance=builder_account)
    with pytest.raises(ValueError):
        assert serializer.data


def test_builder_account_summary_serializer(builder_account):
    """Should produce serialized BuilderAccount on the happy path."""
    serializer = serializers.BuilderAccountSummarySerializer(instance=builder_account)
    assert serializer.data is not None
    assert "token" not in serializer.data, "Token should never appear in summary serializer."


def test_user_account_serializer(user_account):
    """Should produce serialized UserAccount on the happy path."""
    serializer = serializers.UserAccountSerializer(instance=user_account)
    assert serializer.data is not None
