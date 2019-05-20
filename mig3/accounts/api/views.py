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
    write_serializer_class = serializers.UserAccountSerializer
