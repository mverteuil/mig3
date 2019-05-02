from rest_framework.generics import CreateAPIView

from api.permissions import IsBuilder
from .serializers import BuildSerializer


class BuildListView(CreateAPIView):
    """Build listing."""

    serializer_class = BuildSerializer
    permission_classes = (IsBuilder,)
