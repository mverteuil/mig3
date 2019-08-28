from unittest import mock

from django.contrib.auth.models import AnonymousUser

from accounts import models as accounts
from api.permissions import IsBuilder


def test_builder_account():
    """Should require request to be authenticated as a BuilderAccount."""
    authorization = IsBuilder()
    request = mock.MagicMock(name="request", user=AnonymousUser(), auth=mock.Mock(spec=accounts.BuilderAccount))
    assert authorization.has_permission(request, None) is True
    assert authorization.has_object_permission(request, None, None) is True


def test_unauthenticated():
    """Should refuse unauthenticated requests."""
    auth = IsBuilder()
    request = mock.MagicMock(name="request", user=AnonymousUser(), auth=None)
    assert auth.has_permission(request, None) is False
    assert auth.has_object_permission(request, None, None) is False


def test_session():
    """Should refuse session authenticated requests."""
    auth = IsBuilder()
    request = mock.MagicMock(name="request", user=mock.Mock(spec=accounts.UserAccount), auth=None)
    assert auth.has_permission(request, None) is False
    assert auth.has_object_permission(request, None, None) is False
