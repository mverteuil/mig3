from django.contrib.auth import get_user_model

from ..api import serializers


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


def test_builder_account_serializer(builder_account):
    """Should produce serialized BuilderAccount on the happy path."""
    serializer = serializers.BuilderAccountSerializer(instance=builder_account)
    assert serializer.data is not None


def test_user_account_serializer(user_account):
    """Should produce serialized UserAccount on the happy path."""
    serializer = serializers.UserAccountSerializer(instance=user_account)
    assert serializer.data is not None
