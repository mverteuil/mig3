from django.conf import settings
from django.contrib.auth import get_user_model

from hashid_field import rest as hashid_field
from rest_framework import serializers
from rest_framework.fields import empty

from api.serializers import ReadOnlySerializer
from builds import models as builds
from .. import models as accounts


class CurrentBuilderAccount(object):
    """Use the BuilderAccount value from the current request's details."""

    _builder_account: builds.BuilderAccount = None

    def set_context(self, serializer_field):
        """Initialize value for callers."""
        self._builder_account = serializer_field.context["request"].auth

    def __call__(self):
        """Produce value for callers."""
        return self._builder_account


class BuilderStatisticsSerializer(ReadOnlySerializer):
    """Summary API representation for builder relationship counts."""

    build_count = serializers.IntegerField()
    version_count = serializers.IntegerField()


class BuilderAccountSummarySerializer(serializers.ModelSerializer):
    """Summary API representation of a CI/build service."""

    id = hashid_field.HashidSerializerCharField(source_field="accounts.BuilderAccount.id", read_only=True)
    statistics = BuilderStatisticsSerializer(read_only=True)

    class Meta:  # noqa: D106
        model = accounts.BuilderAccount
        fields = ("id", "name", "statistics")


class BuilderAccountSerializer(BuilderAccountSummarySerializer):
    """API representation of a Builder Account.

    Warnings
    --------
    Contains API key in plaintext! For use with administrator views only!
    """

    def __init__(self, instance=None, data=empty, **kwargs):
        try:
            if kwargs["context"]["request"].user.is_superuser:
                super().__init__(instance, data, **kwargs)
            else:
                raise ValueError("Not Administrator")
        except (KeyError, ValueError):
            raise ValueError("Context request with administrator required for viewing BuilderAccount token.")

    class Meta(BuilderAccountSummarySerializer.Meta):  # noqa: D106
        fields = BuilderAccountSummarySerializer.Meta.fields + ("token",)


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

    id = hashid_field.HashidSerializerCharField(source_field="accounts.UserAccount.id", read_only=True)
    is_administrator = serializers.BooleanField(source="is_superuser", read_only=True)

    class Meta:  # noqa: D106
        model = get_user_model()
        fields = ("id", "email", "name", "is_administrator", "build_count")
        read_only_fields = ("build_count",)
        ref_name = "UserAccount"
