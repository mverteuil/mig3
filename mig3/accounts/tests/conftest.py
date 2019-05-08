from django.conf import settings
from django.contrib.auth import get_user_model

import pytest

from accounts import models as accounts


@pytest.fixture
def builder_account(db) -> accounts.BuilderAccount:
    """Create a BuilderAccount fixture."""
    return accounts.BuilderAccount.objects.create(name="Test CI Service")


@pytest.fixture
def user_account(db) -> settings.AUTH_USER_MODEL:
    """Create a UserAccount fixture."""
    return get_user_model().objects.create(email="user@example.com", name="Test User", password="password")


@pytest.fixture
def session_authentication(client, user_account):
    """Create a test client and UserAccount authenticated by session."""
    client.login(username=user_account.email, password="password")
    return (client, user_account)
