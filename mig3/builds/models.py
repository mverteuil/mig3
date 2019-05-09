from dataclasses import dataclass
from typing import Dict, List, Union

from django.conf import settings
from django.db import IntegrityError, models

import django_fsm
import hashid_field
from django_choices_enum import ChoicesEnum
from model_utils.models import TimeStampedModel

from accounts.models import BuilderAccount
from projects.models import Module, Target, Test, Version

DeserializedResult = Dict[str, Union[str, "TestResult"]]
DeserializedResultList = List[DeserializedResult]


class TestResult(int, ChoicesEnum):
    """Enumerate possible test testResult."""

    ERROR = (0, "Error")
    FAILED = (1, "Failed")
    PASSED = (2, "Passed")
    SKIPPED = (3, "Skipped")
    XFAILED = (4, "XFailed")


class Duplicate(IntegrityError):
    """Attempted to introduce duplicate Build result."""


class RegressionDetected(ValueError):
    """Attempted to introduce TestOutcome regression."""

    def __init__(self, test: str, previous_result: "TestResult", current_result: "TestResult"):
        super().__init__(
            f"The build attempted to introduce this regression to your migration: "
            f"{test} ({TestResult(previous_result).name} 👉 {TestResult(current_result).name})"
        )


@dataclass
class OutcomeSummary:
    """Summary of test outcome result counts."""

    error: int
    failed: int
    passed: int
    skipped: int
    xfailed: int


class BuildManager(models.Manager):
    """Manage Build objects."""

    use_for_related_fields = True
    use_in_migrations = True

    def create_build(
        self, number: str, target: Target, version: Version, builder: BuilderAccount, results: DeserializedResultList
    ) -> "Build":
        """Create a new Build with TestOutcomes.

        Raises
        ------
        Duplicate
            Attempted to create a duplicate of an existing Build record.
        RegressionDetected
            Attempted to introduce TestOutcome regression.

        """
        try:
            build = self.model(number=number, target=target, version=version, builder=builder)
            build.save()
        except IntegrityError:
            raise Duplicate((number, version.hash))
        else:
            for result in results:
                module, _ = Module.objects.get_or_create(path=result["module"], project=target.project)
                test, _ = module.test_set.get_or_create(name=result["test"])
                build.testoutcome_set.create(test=test, result=result["result"])
            return build


class Build(TimeStampedModel):
    """Attempt to move the migration state forward, submitted by a builder."""

    id = hashid_field.HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["builds.Build"])
    builder = models.ForeignKey("accounts.BuilderAccount", on_delete=models.CASCADE)
    target = models.ForeignKey("projects.Target", on_delete=models.CASCADE)
    version = models.ForeignKey("projects.Version", on_delete=models.CASCADE)
    number = models.CharField("Build Number", max_length=255, help_text="Execution ID of WorkFlow/Job/Build in Builder")

    objects = BuildManager()

    class Meta:  # noqa: D106
        constraints = (
            models.UniqueConstraint(fields=["number", "target"], name="unique_number_per_target"),
            models.UniqueConstraint(fields=["version", "target"], name="unique_version_per_target"),
        )

    def __str__(self):
        return (
            f"{self.number}: {self.target.project.name} @ "
            f"{self.target.name} on {self.builder.name} ({self.version.hash[:8]})"
        )

    @property
    def modules(self) -> models.QuerySet:
        """Modules under test during this build."""
        return Module.objects.filter(pk__in=self.testoutcome_set.values_list("test__module__id").distinct())

    @property
    def outcome_summary(self) -> OutcomeSummary:
        """Aggregate counts for each TestResult value in related TestOutcomes."""
        aggregates = {result.name.lower(): models.Count("pk", models.Q(result=result.value)) for result in TestResult}
        return OutcomeSummary(**self.testoutcome_set.aggregate(**aggregates))


class TestOutcomeManager(models.Manager):
    """Manage TestOutcome objects."""

    use_for_related_fields = True

    @staticmethod
    def _clone_latest_outcome_for_target(test: Test, target: Target) -> "TestOutcome":
        cloned_outcome = test.testoutcome_set.filter(build__target=target).latest("id")
        cloned_outcome.id = None
        return cloned_outcome

    def _perform_result_transition(self, test: Test, target: Target, result: TestResult) -> "TestOutcome":
        test_outcome = self._clone_latest_outcome_for_target(test, target)
        transition_method_name = f"set_{result.name.lower()}"
        getattr(test_outcome, transition_method_name)()
        test_outcome.save()
        return test_outcome

    def create(self, build: Build, test: Test, result: TestResult) -> "TestOutcome":
        """Create validated test outcome.

        Raises
        ------
        RegressionDetected
            Attempted to introduce TestOutcome regression.

        """
        try:
            return self._perform_result_transition(test, build.target, result)
        except TestOutcome.DoesNotExist:
            return super().create(build=build, test=test, result=result)
        except django_fsm.TransitionNotAllowed as err:
            raise RegressionDetected(str(test), err.object.result, result)


class TestOutcome(TimeStampedModel):
    """Test outcome for which the result moves the migration state forward, was equivalent, or is new."""

    build = models.ForeignKey("builds.Build", on_delete=models.CASCADE)
    test = models.ForeignKey("projects.Test", on_delete=models.CASCADE)
    result = django_fsm.FSMIntegerField(protected=True, choices=TestResult.choices(), default=TestResult.ERROR)

    objects = TestOutcomeManager()

    def __str__(self):
        return f"{self.test}: {TestResult(self.result).name.lower()} as of {self.build}"

    @django_fsm.transition("result", source=[TestResult.ERROR], target=TestResult.ERROR)
    def set_error(self):
        """Set result value to TestResult.ERROR."""
        pass

    @django_fsm.transition("result", source=[TestResult.FAILED], target=TestResult.FAILED)
    def set_failed(self):
        """Set result value to TestResult.FAILED."""
        pass

    @django_fsm.transition("result", source=list(TestResult), target=TestResult.PASSED)
    def set_passed(self):
        """Set result value to TestResult.PASSED."""
        pass

    @django_fsm.transition("result", source=[TestResult.SKIPPED], target=TestResult.SKIPPED)
    def set_skipped(self):
        """Set result value to TestResult.SKIPPED."""
        pass

    @django_fsm.transition(
        "result", source=[TestResult.ERROR, TestResult.FAILED, TestResult.XFAILED], target=TestResult.XFAILED
    )
    def set_xfailed(self):
        """Set result value to TestResult.XFAILED."""
        pass
