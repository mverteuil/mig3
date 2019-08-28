from django.urls import reverse

import pytest
from rest_framework import status


def test_build_list_view_post_with_bearer(
    django_db_reset_sequences, bearer_authentication, serialized_build, primary_target
):
    """Should accept post requests authenticated by bearer token."""
    client, builder_account = bearer_authentication
    url = reverse("api:build_list")
    response = client.post(url, data=serialized_build, format="json")
    assert response.status_code == status.HTTP_201_CREATED, response.data


def test_build_list_view_delete_with_session(
    django_db_reset_sequences, session_authentication, serialized_build, primary_target
):
    """Should refuse delete requests authenticated by session key."""
    client, builder_account = session_authentication
    url = reverse("api:build_list")
    response = client.delete(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_build_list_view_post_with_session(
    django_db_reset_sequences, session_authentication, serialized_build, primary_target
):
    """Should refuse post requests authenticated by session key."""
    client, builder_account = session_authentication
    url = reverse("api:build_list")
    response = client.post(url, data=serialized_build, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_build_detail_view_with_session(primary_build, session_authentication):
    """Should return serialized result."""
    client, user_account = session_authentication
    url = reverse("api:build_detail", kwargs={"build_id": primary_build.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_build_detail_view_without_session(primary_build, client):
    """Should refuse unauthenticated request."""
    url = reverse("api:build_detail", kwargs={"build_id": primary_build.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


#: HTTP methods which modify the object state, other than POST, which is permitted to BuilderAccounts.
BUILD_LIST_INVALID_HTTP_METHODS = ("get", "patch", "put")

#: HTTP methods which modify the object state.
BUILD_DETAIL_INVALID_HTTP_METHODS = ("delete", "patch", "put", "post")


@pytest.mark.parametrize(
    ("view_name", "view_kwargs", "view_methods"),
    (
        ("api:build_list", {}, BUILD_LIST_INVALID_HTTP_METHODS),
        ("api:build_detail", {"build_id": "qL70nKe"}, BUILD_DETAIL_INVALID_HTTP_METHODS),
    ),
)
def test_object_immutability_with_session(primary_build, session_authentication, view_name, view_kwargs, view_methods):
    """Should refuse invalid object operations with session authentication."""
    api_client, _ = session_authentication
    url = reverse(view_name, kwargs=view_kwargs)
    for view_method in view_methods:
        response = getattr(api_client, view_method)(url)
        assert response.status_code in (status.HTTP_405_METHOD_NOT_ALLOWED, status.HTTP_401_UNAUTHORIZED), view_method
