from itertools import product, repeat

import django_fsm
import pytest

from builds.models import TestOutcome

Results = TestOutcome.Results

# All values can transition to themselves
VALID_TRANSITIONS = set(zip(Results, Results))
# All values can transition to Results.PASSED
VALID_TRANSITIONS = VALID_TRANSITIONS.union(zip(Results, repeat(Results.PASSED)))
# Results.ERROR and Results.FAILED can transition to Results.XFAILED
VALID_TRANSITIONS = VALID_TRANSITIONS.union(zip([Results.ERROR, Results.FAILED], repeat(Results.XFAILED)))

# Any combination that isn't valid is therefore invalid
INVALID_TRANSITIONS = set(product(Results, Results)) - VALID_TRANSITIONS


@pytest.mark.parametrize(["initial_value", "target_value"], VALID_TRANSITIONS)
def test_valid_transitions(initial_value, target_value):
    """Should perform value transitions successfully for valid combinations."""
    outcome = TestOutcome(result=initial_value)
    getattr(outcome, f"set_{target_value.name.lower()}")()
    assert outcome.result == target_value


@pytest.mark.parametrize(["initial_value", "target_value"], INVALID_TRANSITIONS)
def test_invalid_transitions(initial_value, target_value):
    """Should raise exception for invalid combinations and leave result in original state."""
    outcome = TestOutcome(result=initial_value)
    with pytest.raises(django_fsm.TransitionNotAllowed):
        getattr(outcome, f"set_{target_value.name.lower()}")()
    assert outcome.result == initial_value, outcome.result
