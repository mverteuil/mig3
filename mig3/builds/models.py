from typing import Dict, List, Union

from django.db import models

import django_fsm
from django_choices_enum import ChoicesEnum
from model_utils.models import TimeStampedModel

from accounts.models import BuilderAccount
from projects.models import Module, Target, Test, Version

DeserializedResult = Dict[str, Union[str, "TestOutcome.Results"]]
DeserializedResultList = List[DeserializedResult]


class RegressionDetected(ValueError):
    """Detected attempt to introduce TestOutcome regression."""

    def __init__(self, test: str, previous_result: "TestOutcome.Results", current_result: "TestOutcome.Results"):
        super().__init__(
            f"The build attempted to introduce this regression to your migration: "
            f"{test} ({TestOutcome.Results(previous_result).name} 👉 {TestOutcome.Results(current_result).name})"
        )


class BuildManager(models.Manager):
    """Manage Build objects."""

    use_for_related_fields = True
    use_in_migrations = True

    def create_build(
        self, number: str, target: Target, version: Version, builder: BuilderAccount, results: DeserializedResultList
    ) -> "Build":
        """Create a new Build with TestOutcomes."""
        build = self.model(number=number, target=target, version=version, builder=builder)
        build.save()
        for result in results:
            module, _ = Module.objects.get_or_create(path=result["module"], project=target.project)
            test, _ = Test.objects.get_or_create(name=result["test"], module=module)
            build.testoutcome_set.create(test=test, result=result["result"])
        return build


class Build(TimeStampedModel):
    """Attempt to move the migration state forward, submitted by a builder."""

    builder = models.ForeignKey("accounts.BuilderAccount", on_delete=models.CASCADE)
    target = models.ForeignKey("projects.Target", on_delete=models.CASCADE)
    version = models.ForeignKey("projects.Version", on_delete=models.CASCADE)
    number = models.CharField("Build Number", max_length=255, help_text="Execution ID of WorkFlow/Job/Build in Builder")

    objects = BuildManager()

    def __str__(self):
        return f"{self.number}: {self.target.project.name} @ {self.target.name} on {self.builder.name} ({self.version.hash[:8]})"


class TestOutcomeManager(models.Manager):
    """Manage TestOutcome objects."""

    use_for_related_fields = True

    @staticmethod
    def _clone_previous_outcome_for_target(test: Test, target: Target) -> "TestOutcome":
        previous_outcome = test.testoutcome_set.filter(build__target=target).latest("id")
        outcome = previous_outcome
        outcome.id = None
        return outcome

    def _perform_result_transition(self, target: Target, test: Test, result: "TestOutcome.Results") -> "TestOutcome":
        outcome = self._clone_previous_outcome_for_target(test, target)
        perform_result_transition = getattr(outcome, f"set_{result.name.lower()}")
        perform_result_transition()
        outcome.save()
        return outcome

    def create(self, build: Build, test: Test, result: "TestOutcome.Results") -> "TestOutcome":
        """Create validated test outcome."""
        try:
            return self._perform_result_transition(test, build.target, result)
        except TestOutcome.DoesNotExist:
            return build.testoutcome_set.create(test=test, result=result)
        except django_fsm.TransitionNotAllowed:
            raise RegressionDetected(str(test), None, None)


class TestOutcome(TimeStampedModel):
    """Test outcome accepted because it moved the migration state forward."""

    class Results(int, ChoicesEnum):
        """Enumerate possible test results."""

        ERROR = (0, "Error")
        FAILED = (1, "Failed")
        PASSED = (2, "Passed")
        SKIPPED = (3, "Skipped")
        XFAILED = (4, "XFailed")

    build = models.ForeignKey("builds.Build", on_delete=models.CASCADE)
    test = models.ForeignKey("projects.Test", on_delete=models.CASCADE)
    result = django_fsm.FSMIntegerField(protected=True, choices=Results.choices(), default=Results.ERROR)

    def __str__(self):
        return f"{self.test}: {self.Results(self.result).name.lower()} as of {self.build}"

    @django_fsm.transition("result", source=[Results.ERROR, Results.FAILED], target=Results.XFAILED)
    def set_xfailed(self):
        """Set result value to Results.XFAILED."""
        pass

    @django_fsm.transition("result", source=Results, target=Results.PASSED)
    def set_passed(self):
        """Set result value to Results.PASSED."""
        pass
