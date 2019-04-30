from unittest import mock

from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APIRequestFactory

from api.authentication import BearerAuthentication


def test_bearer_authentication():
    """Should authenticate BuilderAccount."""
    authentication = BearerAuthentication()

    with mock.patch.object(BearerAuthentication, "model") as BearerModel:
        expected_instance = BearerModel.objects.get()
        request = APIRequestFactory().get("/", HTTP_AUTHORIZATION="Bearer bearer-token")
        user, auth = authentication.authenticate(request)

    assert isinstance(user, AnonymousUser)
    assert auth == expected_instance
