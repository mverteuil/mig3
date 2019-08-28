import copy
import json

import pytest

from builds import models as builds


@pytest.fixture
def better_test_results(test_results) -> builds.DeserializedResultList:
    """Generate deserialized test result list with progression from base case."""
    test_results = copy.deepcopy(test_results)
    for result in test_results:
        if result["result"] != builds.TestResult.PASSED:
            result["result"] = builds.TestResult.PASSED
    return test_results


@pytest.fixture
def serialized_build(shared_datadir):
    """Provide serialized incoming build request data."""
    return json.load(open(shared_datadir / "serialized_build.json"))


@pytest.fixture
def serialized_build_regression(shared_datadir):
    """Provide serialized incoming build request data."""
    return json.load(open(shared_datadir / "serialized_build_regression.json"))


@pytest.fixture
def worse_test_results(test_results) -> builds.DeserializedResultList:
    """Generate deserialized test result list with regression from base case."""
    test_results = copy.deepcopy(test_results)
    for result in test_results:
        if result["result"] != builds.TestResult.FAILED:
            result["result"] = builds.TestResult.FAILED
    return test_results
