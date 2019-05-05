from rest_framework import authentication, generics, permissions

from api.permissions import IsBuilder
from .serializers import BuildSerializer


class BuildDetailView(generics.RetrieveAPIView):
    """Build details."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = permissions.IsAuthenticated
    serializer_class = BuildSerializer


class BuildListView(generics.CreateAPIView):
    """Build listing."""

    permission_classes = (IsBuilder,)
    serializer_class = BuildSerializer
