from django.contrib.auth import get_user_model

from rest_framework import authentication, generics, permissions

from .. import models as accounts
from . import serializers


class BuilderAccountList(generics.ListAPIView):
    """List Builder Accounts."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = accounts.BuilderAccount.objects.all()
    serializer_class = serializers.BuilderAccountSerializer


class UserAccountList(generics.ListAPIView):
    """List User Accounts."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserAccountSerializer
