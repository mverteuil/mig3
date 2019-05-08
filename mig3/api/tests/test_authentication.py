from unittest import mock

from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist

import pytest
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.test import APIRequestFactory

from api.authentication import BearerAuthentication


def test_bearer_authentication_success():
    """Should authenticate BuilderAccount."""
    authentication = BearerAuthentication()

    with mock.patch.object(BearerAuthentication, "model") as BearerModel:
        expected_instance = BearerModel.objects.get()
        request = APIRequestFactory().get("/", HTTP_AUTHORIZATION="Bearer bearer-token")
        user, auth = authentication.authenticate(request)

    assert isinstance(user, AnonymousUser)
    assert auth == expected_instance


def test_bearer_authentication_failure():
    """Should fail to authenticate with invalid credentials."""
    authentication = BearerAuthentication()

    with mock.patch.object(BearerAuthentication, "model") as BearerModel:
        BearerModel.objects.get.side_effect = [ObjectDoesNotExist]
        request = APIRequestFactory().get("/", HTTP_AUTHORIZATION="Bearer bearer-token")
        with pytest.raises(AuthenticationFailed):
            authentication.authenticate(request)
