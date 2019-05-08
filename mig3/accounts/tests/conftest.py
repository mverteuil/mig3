from django.conf import settings
from django.contrib.auth import get_user_model

import pytest
from rest_framework.test import APIClient

from accounts import models as accounts


@pytest.fixture
def api_client():
    """Create an unauthenticated API test client."""
    return APIClient()


@pytest.fixture
def builder_account(db) -> accounts.BuilderAccount:
    """Create a BuilderAccount."""
    return accounts.BuilderAccount.objects.create(name="Test CI Service")


@pytest.fixture
def user_account(db) -> settings.AUTH_USER_MODEL:
    """Create a UserAccount."""
    return get_user_model().objects.create_user(name="Test User", email="user@example.com", password="password")


@pytest.fixture
def session_authentication(api_client, user_account):
    """Create a test client and UserAccount authenticated by session."""
    api_client.login(username=user_account.email, password="password")
    return (api_client, user_account)
