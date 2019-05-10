from django.conf import settings
from django.contrib.auth import get_user_model

from hashid_field import rest as hashid_field
from rest_framework import serializers

from .. import models as accounts


class BuilderAccountSerializer(serializers.ModelSerializer):
    """API representation of a CI/build service."""

    id = hashid_field.HashidSerializerCharField(source_field="accounts.BuilderAccount.id")

    class Meta:  # noqa: D106
        model = accounts.BuilderAccount
        fields = ("id", "name")


class UserAccountField(serializers.Field):
    """Consume author details for a Build submitted through the API.

    Will create a new inactive UserAccount for the author if the email has not been seen before.
    """

    def to_internal_value(self, data: str) -> settings.AUTH_USER_MODEL:
        """Deserialize author for storage."""
        UserAccount = get_user_model()
        try:
            return UserAccount.objects.get_by_natural_key(data)
        except UserAccount.DoesNotExist:
            return UserAccount.objects.create_user(email=data)

    def to_representation(self, value) -> str:
        """Serialize author for representation."""
        return str(value)


class UserAccountSerializer(serializers.ModelSerializer):
    """API representation of a user account."""

    id = hashid_field.HashidSerializerCharField(source_field="accounts.UserAccount.id")

    class Meta:  # noqa: D106
        model = get_user_model()
        fields = ("id", "email", "name", "build_count")
