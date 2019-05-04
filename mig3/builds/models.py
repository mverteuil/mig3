from django.db import models

import django_fsm
from django_choices_enum import ChoicesEnum
from model_utils.models import TimeStampedModel

from accounts import models as accounts
from projects import models as projects


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


class BuildManager(models.Manager):
    """Manage Build objects."""

    use_for_related_fields = True
    use_in_migrations = True

    def create_build(
        self,
        number: str,
        target: projects.Target,
        version: projects.Version,
        builder: accounts.BuilderAccount,
        results: list,
    ) -> "Build":
        """Create a new Build with TestOutcomes."""
        build = self.model(number=number, target=target, version=version, builder=builder)
        build.save()
        for test_result in results:
            module, _ = target.project.module_set.get_or_create(path=test_result["test__module__path"])
            test, _ = module.test_set.get_or_create(name=test_result["test__name"])
            build.create_test_outcome(test, test_result["result"])
        return build


class Build(TimeStampedModel):
    """Attempt to move the migration state forward, submitted by a builder."""

    class RegressionDetected(ValueError):
        """Attempted to introduce regression with build."""

        def __init__(self, test, previous_result, current_result):
            super().__init__(
                f"The build attempted to introduce this regression to your migration: "
                f"{test} ({TestOutcome.Results(previous_result).name} 👉 {TestOutcome.Results(current_result).name})"
            )

    builder = models.ForeignKey("accounts.BuilderAccount", on_delete=models.CASCADE)
    target = models.ForeignKey("projects.Target", on_delete=models.CASCADE)
    version = models.ForeignKey("projects.Version", on_delete=models.CASCADE)
    number = models.CharField("Build Number", max_length=255, help_text="Execution ID of WorkFlow/Job/Build in Builder")

    objects = BuildManager()

    def __str__(self):
        return f"{self.number}: {self.target.project.name} @ {self.target.name} on {self.builder.name} ({self.version.hash[:8]})"

    def create_test_outcome(self, test: projects.Test, result: TestOutcome.Results) -> TestOutcome:
        """Create validated test outcome."""
        try:
            previous_outcome = test.testoutcome_set.filter(build__target=self.target).latest("id")
            outcome = previous_outcome
            outcome.id = None
            try:
                field_transition = getattr(outcome, f"set_{result.name.lower()}")
                field_transition()
            except django_fsm.TransitionNotAllowed:
                raise self.RegressionDetected(test, previous_outcome.result, result)

            outcome.save()
            return outcome
        except TestOutcome.DoesNotExist:
            return self.testoutcome_set.create(test=test, result=result)
