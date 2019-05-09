from django.urls import reverse

import pytest
from rest_framework import status

#: HTTP methods which modify the object state.
INVALID_HTTP_METHODS = ("delete", "patch", "put", "post")


@pytest.mark.parametrize(
    ("view_name", "view_kwargs"),
    (
        ("api:project_list", {}),
        ("api:project_detail", {"project_id": "qL70nKe"}),
        ("api:target_build_list", {"target_id": "qL70nKe"}),
    ),
)
@pytest.mark.parametrize("view_method", INVALID_HTTP_METHODS)
def test_object_immutability(project, target, session_authentication, view_name, view_kwargs, view_method):
    """Should refuse invalid object operations with session authentication."""
    api_client, _ = session_authentication
    url = reverse(view_name, kwargs=view_kwargs)
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.parametrize(
    ("view_name", "view_kwargs"),
    (
        ("api:project_list", {}),
        ("api:project_detail", {"project_id": "qL70nKe"}),
        ("api:target_build_list", {"target_id": "qL70nKe"}),
    ),
)
def test_view_with_session(project, target, session_authentication, view_name, view_kwargs):
    """Should accept authenticated requests."""
    api_client, _ = session_authentication
    url = reverse(view_name, kwargs=view_kwargs)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize(
    ("view_name", "view_kwargs"),
    (
        ("api:project_list", {}),
        ("api:project_detail", {"project_id": "qL70nKe"}),
        ("api:target_build_list", {"target_id": "qL70nKe"}),
    ),
)
def test_view_without_session(project, target, client, view_name, view_kwargs):
    """Should refuse unauthenticated requests."""
    url = reverse(view_name, kwargs=view_kwargs)
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
