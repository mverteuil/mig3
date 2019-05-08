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


class UserAccountSerializer(serializers.ModelSerializer):
    """API representation of a user account."""

    id = hashid_field.HashidSerializerCharField(source_field="accounts.UserAccount.id")

    class Meta:  # noqa: D106
        model = get_user_model()
        fields = ("id", "email", "name")
