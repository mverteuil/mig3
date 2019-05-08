from django.urls import reverse

import pytest
from rest_framework import status


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
def test_view_with_session(session_authentication, view_name):
    """Should return serialized result."""
    client, user_account = session_authentication
    url = reverse(view_name)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize("view_name", ["api:user_account_list", "api:builder_account_list"])
def test_view_without_session(client, view_name):
    """Should refuse unauthenticated request."""
    url = reverse(view_name)
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
