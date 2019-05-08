import copy
import json

import pytest

from accounts import models as accounts
from builds import models as builds
from projects import models as projects


@pytest.fixture
def another_version(version) -> projects.Version:
    """Create a second Version from the original Version's author."""
    return version.author.version_set.create(hash="b2" * 20)


@pytest.fixture
def better_test_results(test_results) -> builds.DeserializedResultList:
    """Generate deserialized test result list with progression from base case."""
    test_results = copy.deepcopy(test_results)
    for result in test_results:
        if result["result"] != builds.TestOutcome.Results.PASSED:
            result["result"] = builds.TestOutcome.Results.PASSED
    return test_results


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
def serialized_build(shared_datadir):
    """Provide serialized incoming build request data."""
    return json.load(open(shared_datadir / "serialized_build.json"))


@pytest.fixture
def serialized_build_regression(shared_datadir):
    """Provide serialized incoming build request data."""
    return json.load(open(shared_datadir / "serialized_build_regression.json"))


@pytest.fixture
def target(db) -> projects.Target:
    """Create a Project and Target."""
    project = projects.Project.objects.create(name="Test Project")
    return project.target_set.create(name="Test Target")


@pytest.fixture
def test_results() -> builds.DeserializedResultList:
    """Generate deserialized test result list base case."""
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


@pytest.fixture
def worse_test_results(test_results) -> builds.DeserializedResultList:
    """Generate deserialized test result list with regression from base case."""
    test_results = copy.deepcopy(test_results)
    for result in test_results:
        if result["result"] != builds.TestOutcome.Results.FAILED:
            result["result"] = builds.TestOutcome.Results.FAILED
    return test_results
