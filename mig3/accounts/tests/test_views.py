from django.urls import reverse

import pytest
from rest_framework import status


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
def test_view_with_session(session_authentication, view_name):
    """Should return serialized result."""
    client, _ = session_authentication
    url = reverse(view_name)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
def test_view_without_session(client, view_name):
    """Should refuse unauthenticated request."""
    url = reverse(view_name)
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


#: HTTP methods which modify the object state
INVALID_HTTP_METHODS = ("delete", "patch", "put", "post")


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
@pytest.mark.parametrize("view_method", INVALID_HTTP_METHODS)
def test_object_immutability_with_session(session_authentication, view_name, view_method):
    """Should refuse to mutate object with session authentication."""
    api_client, _ = session_authentication
    url = reverse(view_name)
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_login(client, user_account, webpack_safe):
    """Should create session for active users."""
    url = reverse("login")
    response = client.post(url, data={"username": user_account.email, "password": "password"}, follow=True)
    assert response.status_code == status.HTTP_200_OK


def test_login_without_account(client, db):
    """Should require valid credentials to create login session."""
    url = reverse("login")
    response = client.post(url, data={"username": "user@example.com", "password": "password"})
    assert response.status_code == status.HTTP_200_OK
    assert "Please enter a correct Email Address" in str(response.content)


def test_login_with_inactive_account(client, user_account):
    """Should require active account to create login session."""
    user_account.is_active = False
    user_account.save()

    url = reverse("login")
    response = client.post(url, data={"username": user_account.email, "password": "password"}, follow=True)
    assert response.status_code == status.HTTP_200_OK
    assert "Please enter a correct Email Address" in str(response.content)
