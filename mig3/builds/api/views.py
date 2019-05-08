from rest_framework import authentication, generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.permissions import IsBuilder
from .. import models as builds
from . import serializers as serializers


class BuildDetailView(generics.RetrieveAPIView):
    """Build details."""

    authentication_classes = (authentication.SessionAuthentication,)
    lookup_url_kwarg = "build_id"
    permission_classes = (permissions.IsAuthenticated,)
    queryset = builds.Build.objects.all()
    serializer_class = serializers.BuildReadSerializer


class BuildListView(generics.CreateAPIView):
    """Build listing."""

    permission_classes = (IsBuilder,)
    serializer_class = serializers.BuildWriteSerializer

    def create(self, request, *args, **kwargs):
        """Accept mig3-client build submissions."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)


class TargetBuildListView(generics.ListAPIView):
    """Build listing for a configuration target."""

    authentication_classes = (authentication.SessionAuthentication,)
    lookup_field = "target"
    permission_classes = (IsAuthenticated,)
    queryset = builds.Build.objects.all()
    serializer_class = serializers.BuildSummarySerializer
