from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import authentication, generics, permissions

from .. import models as accounts
from . import serializers


class BuilderAccountDetailView(generics.RetrieveAPIView):
    """Retrieve Builder Account Details."""

    authentication_classes = (authentication.SessionAuthentication,)
    lookup_url_kwarg = "builder_id"
    permission_classes = (permissions.IsAdminUser,)
    queryset = accounts.BuilderAccount.objects.all()
    serializer_class = serializers.BuilderAccountSerializer


class BuilderAccountListView(generics.ListCreateAPIView):
    """List Builder Accounts."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAuthenticated)
    queryset = accounts.BuilderAccount.objects.all()
    serializer_class = serializers.BuilderAccountSummarySerializer


class UserAccountListView(generics.ListCreateAPIView):
    """List User Accounts."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAuthenticated)
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserAccountSerializer


class RequestUserAccountDetailView(generics.RetrieveAPIView):
    """Retrieve User Account Details for Request User."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserAccountSerializer

    def get_object(self) -> settings.AUTH_USER_MODEL:
        """Reflect the request user back as serialized details."""
        return self.request.user
