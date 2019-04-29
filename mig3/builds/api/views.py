from rest_framework.generics import CreateAPIView

from .serializers import BuildSerializer


class BuildListView(CreateAPIView):
    """Build listing."""

    serializer_class = BuildSerializer
