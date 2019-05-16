from typing import Callable, Tuple

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase

import pytest
from rest_framework.test import APIClient
from webpack_loader.loader import WebpackLoader

from accounts import models as accounts
from builds import models as builds
from projects import models as projects


@pytest.fixture
def admin_user(db) -> settings.AUTH_USER_MODEL:
    """Create a superuser account."""
    return get_user_model().objects.create_superuser(email="admin@example.com", password="password")


@pytest.fixture
def another_version(version) -> projects.Version:
    """Create a second Version from the original Version's author."""
    return version.author.version_set.create(hash="b2" * 20)


@pytest.fixture
def api_client() -> APIClient:
    """Create an unauthenticated API test client."""
    return APIClient()


@pytest.fixture
def assert_redirects() -> Callable:
    """Provide redirect assertion."""
    return SimpleTestCase().assertRedirects


@pytest.fixture
def bearer_authentication(api_client, builder_account) -> Tuple[APIClient, accounts.BuilderAccount]:
    """Create a test client and BuilderAccount authenticated by bearer token."""
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {builder_account.token}")
    return api_client, builder_account


@pytest.fixture
def webpack_safe(monkeypatch):
    """Patch webpack for views that interact with it."""
    monkeypatch.setattr(WebpackLoader, "get_bundle", lambda loader, bundle_name: [])


@pytest.fixture
def build(db, target, version, builder_account, test_results) -> builds.Build:
    """Create a fully populated Build.

    Includes: Project, Target, BuilderAccount, Modules, Tests, TestOutcomes
    """
    return builds.Build.objects.create_build("1", target, version, builder_account, test_results)


@pytest.fixture
def builder_account(db) -> accounts.BuilderAccount:
    """Create a BuilderAccount."""
    return accounts.BuilderAccount.objects.create(name="Test CI Service")


@pytest.fixture
def project(db) -> projects.Project:
    """Create a Project."""
    return projects.Project.objects.create(name="Test Project")


@pytest.fixture
def user_account(db) -> settings.AUTH_USER_MODEL:
    """Create a UserAccount."""
    return get_user_model().objects.create_user(name="Test User", email="user@example.com", password="password")


@pytest.fixture
def session_authentication(api_client, user_account) -> Tuple[APIClient, settings.AUTH_USER_MODEL]:
    """Create a test client and UserAccount authenticated by session."""
    api_client.login(username=user_account.email, password="password")
    return api_client, user_account


@pytest.fixture
def target(db) -> projects.Target:
    """Create a Project and Target."""
    project = projects.Project.objects.create(name="Test Project")
    return project.target_set.create(name="Test Target")


@pytest.fixture
def test_results() -> builds.DeserializedResultList:
    """Generate deserialized test result list base case."""
    return [
        {"module": "tests/test_example01.py", "test": "test_error", "result": builds.TestResult.ERROR},
        {"module": "tests/test_example01.py", "test": "test_failed", "result": builds.TestResult.FAILED},
        {"module": "tests/test_example01.py", "test": "test_passed", "result": builds.TestResult.PASSED},
        {"module": "tests/test_example01.py", "test": "test_skipped", "result": builds.TestResult.SKIPPED},
        {"module": "tests/test_example01.py", "test": "test_xfailed", "result": builds.TestResult.XFAILED},
        {"module": "tests/test_example02.py", "test": "test_error", "result": builds.TestResult.ERROR},
        {"module": "tests/test_example02.py", "test": "test_failed", "result": builds.TestResult.FAILED},
        {"module": "tests/test_example02.py", "test": "test_passed", "result": builds.TestResult.PASSED},
        {"module": "tests/test_example02.py", "test": "test_skipped", "result": builds.TestResult.SKIPPED},
        {"module": "tests/test_example02.py", "test": "test_xfailed", "result": builds.TestResult.XFAILED},
    ]


@pytest.fixture
def version(db) -> projects.Version:
    """Create a UserAccount and Version."""
    version_user = accounts.UserAccount.objects.create_user(email="author@example.com")
    return version_user.version_set.create(hash="a1" * 20)
