from unittest import mock

from django.contrib.auth import get_user_model
from django.urls import reverse

import pytest
from rest_framework import status

#: HTTP methods which operate on a detail endpoint
MUTATING_HTTP_DETAIL_METHODS = ("delete", "patch", "put")

#: HTTP methods which operate on a list endpoint
MUTATING_HTTP_LIST_METHODS = ("post",)


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


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
@pytest.mark.parametrize("view_method", MUTATING_HTTP_DETAIL_METHODS)
def test_invalid_list_methods(admin_user, session_authentication, view_name, view_method):
    """Should refuse operations that don't make sense."""
    api_client, _ = session_authentication
    url = reverse(view_name)
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    api_client.login(username=admin_user.email, password="password")
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
@pytest.mark.parametrize("view_method", MUTATING_HTTP_LIST_METHODS)
def test_object_immutability_with_user(session_authentication, view_name, view_method):
    """Should refuse to mutate object with session authentication."""
    api_client, _ = session_authentication
    url = reverse(view_name)
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
@pytest.mark.parametrize("view_method", MUTATING_HTTP_LIST_METHODS)
def test_object_mutability_with_admin_session(admin_user, api_client, view_name, view_method):
    """Should allow administrator to mutate object."""
    api_client.login(username=admin_user.email, password="password")
    url = reverse(view_name)
    response = getattr(api_client, view_method)(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_builder_account_detail_with_admin_session(admin_user, api_client, builder_account):
    """Should allow administrator to view Builder Account token in plain text."""
    api_client.login(username=admin_user.email, password="password")
    url = reverse("api:builder_account_detail", kwargs={"builder_id": builder_account.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["token"] == builder_account.token


def test_builder_account_detail_with_user_session(builder_account, session_authentication):
    """Should refuse to view Builder Account token in plain text as standard user."""
    api_client, _ = session_authentication
    url = reverse("api:builder_account_detail", kwargs={"builder_id": builder_account.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "token" not in response.data


def test_login(client, user_account, webpack_safe):
    """Should create session for active users."""
    url = reverse("login", current_app="accounts")
    response = client.post(url, data={"username": user_account.email, "password": "password"}, follow=True)
    assert response.status_code == status.HTTP_200_OK


def test_login_without_account(client, db, admin_user):
    """Should require valid credentials to create login session."""
    url = reverse("login", current_app="accounts")
    response = client.post(url, data={"username": "user@example.com", "password": "password"})
    assert response.status_code == status.HTTP_200_OK
    assert "Please enter a correct Email Address" in str(response.content)


def test_login_with_inactive_account(admin_user, client, user_account):
    """Should require active account to create login session."""
    user_account.is_active = False
    user_account.save()

    url = reverse("login")
    response = client.post(url, data={"username": user_account.email, "password": "password"}, follow=True)
    assert response.status_code == status.HTTP_200_OK
    assert "Please enter a correct Email Address" in str(response.content)


@mock.patch("accounts.views.URLSignature")
def test_administrator_view_guard_with_valid_signature(patched_signatures, client):
    """Should allow user to visit administrator form with valid signature."""
    url = reverse("create_admin", kwargs={"secret_code": "valid signature"})
    patched_signatures.validate_signature.return_value = True
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@mock.patch("accounts.views.forms.SecretCodeForm")
def test_administrator_view_guard_with_invalid_signature(patched_form, assert_redirects, client):
    """Should refuse to visit administrator form with invalid signature."""
    url = reverse("create_admin", kwargs={"secret_code": "invalid signature"})
    patched_form().is_valid.return_value = False
    response = client.get(url)
    assert response.status_code == status.HTTP_302_FOUND
    assert_redirects(response=response, expected_url=reverse("secret_code"))


@mock.patch("accounts.views.forms.SecretCodeForm")
def test_administrator_create_view(patched_form, allow_stupid_passwords, assert_redirects, client, db):
    """Should allow user to create administrator with valid signature."""
    url = reverse("create_admin", kwargs={"secret_code": ""})
    patched_form().is_valid.return_value = True
    user_data = {
        "email": "admin@example.com",
        "name": "Test Administrator",
        "password1": "password",
        "password2": "password",
    }
    response = client.post(url, data=user_data, follow=False)
    assert_redirects(response=response, expected_url=reverse("bridge"))
    assert get_user_model().objects.filter(is_superuser=True).count() == 1
