from django.urls import reverse

import pytest
from rest_framework import status

#: HTTP methods which operate on a detail endpoint
MUTATING_HTTP_DETAIL_METHODS = ("delete", "patch", "put")


@pytest.mark.parametrize("view_method", MUTATING_HTTP_DETAIL_METHODS)
def test_invalid_list_methods(admin_user, session_authentication, view_method):
    """Should refuse operations that don't make sense."""
    api_client, _ = session_authentication
    url = reverse("api:project_list")
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    api_client.login(username=admin_user.email, password="password")
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.parametrize(
    ("view_name", "view_kwargs"),
    (("api:project_detail", {"project_id": "qL70nKe"}), ("api:target_detail", {"target_id": "qL70nKe"})),
)
@pytest.mark.parametrize("view_method", MUTATING_HTTP_DETAIL_METHODS)
def test_object_immutability_with_user_session(
    primary_target, project, session_authentication, view_name, view_kwargs, view_method
):
    """Should refuse invalid object operations with session authentication."""
    api_client, _ = session_authentication
    url = reverse(view_name, kwargs=view_kwargs)
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.parametrize(
    ("view_name", "view_kwargs"), (("api:project_list", {}), ("api:project_target_list", {"project_id": "qL70nKe"}))
)
def test_object_creation_with_admin_session(
    admin_user, api_client, django_db_reset_sequences, project, view_name, view_kwargs
):
    """Should allow administrator to create objects."""
    api_client.login(username=admin_user.email, password="password")
    url = reverse(view_name, kwargs=view_kwargs)
    response = api_client.post(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize(
    ("view_name", "view_kwargs"), (("api:project_list", {}), ("api:project_target_list", {"project_id": "qL70nKe"}))
)
def test_object_creation_with_user_session(
    django_db_reset_sequences, project, session_authentication, view_name, view_kwargs
):
    """Should allow administrator to create objects."""
    api_client, _ = session_authentication
    url = reverse(view_name, kwargs=view_kwargs)
    response = api_client.post(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize(
    ("view_name", "view_kwargs"),
    (
        ("api:project_list", {}),
        ("api:project_detail", {"project_id": "qL70nKe"}),
        ("api:target_detail", {"target_id": "qL70nKe"}),
    ),
)
def test_view_with_session(
    django_db_reset_sequences, primary_target, project, session_authentication, view_name, view_kwargs
):
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
        ("api:target_detail", {"target_id": "qL70nKe"}),
    ),
)
def test_view_without_session(client, django_db_reset_sequences, primary_target, project, view_name, view_kwargs):
    """Should refuse unauthenticated requests."""
    url = reverse(view_name, kwargs=view_kwargs)
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
