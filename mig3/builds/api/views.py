from django.utils.decorators import method_decorator

from drf_yasg.openapi import Response as ResponseSchema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication, generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.authentication import BearerAuthentication
from api.permissions import IsBuilder
from api.serializers import EmptySerializer, ErrorSerializer
from .. import models as builds
from . import serializers as serializers


class BuildDetailView(generics.RetrieveAPIView):
    """Build details."""

    authentication_classes = (authentication.SessionAuthentication,)
    lookup_url_kwarg = "build_id"
    permission_classes = (permissions.IsAuthenticated,)
    queryset = builds.Build.objects.all()
    serializer_class = serializers.BuildReadSerializer


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: ResponseSchema(description="Build accepted.", schema=EmptySerializer),
            status.HTTP_400_BAD_REQUEST: ResponseSchema(description="Duplicate detected.", schema=ErrorSerializer),
            status.HTTP_409_CONFLICT: ResponseSchema(description="Regression detected.", schema=ErrorSerializer),
        }
    ),
)
class BuildListView(generics.CreateAPIView):
    """Build listing."""

    authentication_classes = (BearerAuthentication,)
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
