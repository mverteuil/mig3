from rest_framework import authentication, generics, permissions

from .. import models as projects
from . import serializers


class ProjectTargetListView(generics.CreateAPIView):
    """Create Project Targets."""

    authentication_classes = (authentication.SessionAuthentication,)
    lookup_field = "project"
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAuthenticated)
    queryset = projects.Target.objects.all()
    serializer_class = serializers.TargetWriteSerializer


class ProjectListView(generics.ListCreateAPIView):
    """List Projects."""

    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAuthenticated)
    queryset = projects.Project.objects.all()
    serializer_class = serializers.ProjectSummarySerializer


class ProjectDetailView(generics.RetrieveAPIView):
    """Retrieve Project Details."""

    authentication_classes = (authentication.SessionAuthentication,)
    lookup_url_kwarg = "project_id"
    permission_classes = (permissions.IsAuthenticated,)
    queryset = projects.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class TargetDetailView(generics.RetrieveAPIView):
    """Retrieve Project Target Details."""

    authentication_classes = (authentication.SessionAuthentication,)
    lookup_url_kwarg = "target_id"
    permission_classes = (permissions.IsAuthenticated,)
    queryset = projects.Target.objects.all()
    serializer_class = serializers.TargetSerializer
