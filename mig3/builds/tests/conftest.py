import pytest

from accounts import models as accounts
from builds import models as builds
from projects import models as projects


@pytest.fixture
def builder_account(db) -> accounts.BuilderAccount:
    """Create a BuilderAccount fixture."""
    return accounts.BuilderAccount.objects.create(name="Test CI Service")


@pytest.fixture
def target(db) -> projects.Target:
    """Create a Project and Target."""
    project = projects.Project.objects.create(name="Test Project")
    return project.target_set.create(name="Test Target")


@pytest.fixture
def test_results() -> builds.DeserializedResultList:
    """Generate deserialized test result list."""
    return [
        {"module": "tests/test_example01.py", "test": "test_error", "result": builds.TestOutcome.Results.ERROR},
        {"module": "tests/test_example01.py", "test": "test_failed", "result": builds.TestOutcome.Results.FAILED},
        {"module": "tests/test_example01.py", "test": "test_passed", "result": builds.TestOutcome.Results.PASSED},
        {"module": "tests/test_example01.py", "test": "test_skipped", "result": builds.TestOutcome.Results.SKIPPED},
        {"module": "tests/test_example01.py", "test": "test_xfailed", "result": builds.TestOutcome.Results.XFAILED},
        {"module": "tests/test_example02.py", "test": "test_error", "result": builds.TestOutcome.Results.ERROR},
        {"module": "tests/test_example02.py", "test": "test_failed", "result": builds.TestOutcome.Results.FAILED},
        {"module": "tests/test_example02.py", "test": "test_passed", "result": builds.TestOutcome.Results.PASSED},
        {"module": "tests/test_example02.py", "test": "test_skipped", "result": builds.TestOutcome.Results.SKIPPED},
        {"module": "tests/test_example02.py", "test": "test_xfailed", "result": builds.TestOutcome.Results.XFAILED},
    ]


@pytest.fixture
def version(db) -> projects.Version:
    """Create a UserAccount and Version."""
    version_user = accounts.UserAccount.objects.create_user(email="author@example.com")
    return version_user.version_set.create(hash="a1" * 20)
