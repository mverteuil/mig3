from django.db import models
from django_choices_enum.base import ChoicesEnum
from model_utils.models import TimeStampedModel


class Build(TimeStampedModel):
    """Attempt to move the migration state forward, submitted by a builder."""

    builder = models.ForeignKey("accounts.Builder", on_delete=models.CASCADE)
    target = models.ForeignKey("projects.Target", on_delete=models.CASCADE)
    version = models.ForeignKey("projects.Version", on_delete=models.CASCADE)
    number = models.CharField("Build Number", max_length=255, help_text="Execution ID of WorkFlow/Job/Build in Builder")


class TestOutcome(TimeStampedModel):
    """Test outcome accepted because it moved the migration state forward."""

    class Results(int, ChoicesEnum):
        ERROR = (0, "Error")
        FAIL = (1, "Failed")
        PASS = (2, "Passed")
        SKIP = (3, "Skipped")
        XFAIL = (4, "XFailed")

    build = models.ForeignKey("builds.Build", on_delete=models.CASCADE)
    test = models.ForeignKey("projects.Test", on_delete=models.CASCADE)
    result = models.IntegerField(choices=Results.choices())
