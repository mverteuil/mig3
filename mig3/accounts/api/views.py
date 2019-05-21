from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import authentication, generics, permissions

from .. import models as accounts
from . import serializers


class BuilderAccountList(generics.ListCreateAPIView):
    """List Builder Accounts."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAuthenticated)
    queryset = accounts.BuilderAccount.objects.all()
    serializer_class = serializers.BuilderAccountSerializer


class UserAccountList(generics.ListCreateAPIView):
    """List User Accounts."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAuthenticated)
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserAccountSerializer


class RequestUserAccountDetail(generics.RetrieveAPIView):
    """Retrieve User Account Detail for Request User."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserAccountSerializer

    def get_object(self) -> settings.AUTH_USER_MODEL:
        """Reflect the request user back as serialized details."""
        return self.request.user
