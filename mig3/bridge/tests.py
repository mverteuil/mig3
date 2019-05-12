from django.http import QueryDict
from django.urls import reverse

from rest_framework import status


def test_bridge_view_with_session(client, user_account, webpack_safe):
    """Should require a session to visit bridge view."""
    url = reverse("bridge")
    client.login(username=user_account.email, password="password")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_bridge_view_without_session(assert_redirects, client, db):
    """Should require a session to visit bridge view."""
    bridge_url = reverse("bridge")
    query = QueryDict(mutable=True)
    query["next"] = bridge_url
    login_url = "?".join((reverse("login"), query.urlencode(safe="utf-8")))

    response = client.get(bridge_url, follow=False)
    assert_redirects(response=response, expected_url=login_url)
