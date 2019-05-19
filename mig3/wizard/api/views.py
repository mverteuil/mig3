from rest_framework import authentication, generics
from rest_framework.permissions import IsAdminUser

from .. import models as wizard
from . import serializers


class InstallationSetupDetailView(generics.RetrieveAPIView):
    """Retrieve installation setup details."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.InstallationSetupSerializer

    def get_object(self):
        """Get InstallationSetup singleton."""
        return wizard.InstallationSetup
