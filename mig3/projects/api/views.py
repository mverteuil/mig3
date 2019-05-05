from rest_framework import authentication, generics, permissions

from .. import models as projects
from . import serializers


class ProjectListView(generics.ListAPIView):
    """List Projects."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = projects.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class TargetDetailView(generics.RetrieveAPIView):
    """Retrieve Project Target Details."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = projects.Target.objects.all()
    serializer_class = serializers.TargetSerializer
