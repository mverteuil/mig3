from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

from ..permissions import IsBuilder


class BuilderAccountPermissionsView(APIView):
    permission_classes = (IsBuilder,)


def test_builder_account():
    factory = APIRequestFactory()
    request = factory.get("/", headers={"Authorization": "Bearer bearer-token"})
    view = BuilderAccountPermissionsView.as_view()
    authorization = IsBuilder()
    assert authorization.has_permission(request, view)
    assert authorization.has_object_permission(request, view, None)
