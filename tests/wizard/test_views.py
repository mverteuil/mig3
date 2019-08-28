from django.urls import reverse

from rest_framework import status


def test_view_with_admin_session(admin_user, api_client):
    """Should permit administrator to retrieve the setup wizard state."""
    api_client.login(username=admin_user.email, password="password")
    url = reverse("api:installation_setup_detail")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert "requirements" in response.data


def test_view_with_session(session_authentication):
    """Should refuse non-administrator requests."""
    client, _ = session_authentication
    url = reverse("api:installation_setup_detail")
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_view_without_session(api_client):
    """Should refuse unauthenticated request."""
    url = reverse("api:installation_setup_detail")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
