from django.db import models
from django_choices_enum import ChoicesEnum
from model_utils.models import TimeStampedModel


class Build(TimeStampedModel):
    """Attempt to move the migration state forward, submitted by a builder."""

    builder = models.ForeignKey("accounts.BuilderAccount", on_delete=models.CASCADE)
    target = models.ForeignKey("projects.Target", on_delete=models.CASCADE)
    version = models.ForeignKey("projects.Version", on_delete=models.CASCADE)
    number = models.CharField("Build Number", max_length=255, help_text="Execution ID of WorkFlow/Job/Build in Builder")

    def __str__(self):
        return f"{self.number}: {self.target.project.name} @ {self.target.name} on {self.builder.name} ({self.version.hash[:8]})"


class TestOutcome(TimeStampedModel):
    """Test outcome accepted because it moved the migration state forward."""

    class Results(int, ChoicesEnum):
        ERROR = (0, "Error")
        FAILED = (1, "Failed")
        PASSED = (2, "Passed")
        SKIPPED = (3, "Skipped")
        XFAILED = (4, "XFailed")

    build = models.ForeignKey("builds.Build", on_delete=models.CASCADE)
    test = models.ForeignKey("projects.Test", on_delete=models.CASCADE)
    result = models.IntegerField(choices=Results.choices())

    def __str__(self):
        return f"{self.test}: {dict(self.Results)[self.result].lower()} as of {self.build}"
