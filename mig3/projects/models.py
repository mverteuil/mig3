from dataclasses import dataclass

from django.conf import settings
from django.db import models

from hashid_field import HashidAutoField
from model_utils.models import TimeStampedModel


@dataclass
class ProjectStatistics:
    """Aggregated Project Statistics."""

    target_count: int
    module_count: int
    test_count: int


class Project(TimeStampedModel):
    """Project undergoing migration from a target to one or more other targets."""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["projects.Project"])
    name = models.CharField("Project Name", max_length=255)
    repo_url = models.URLField("Repository URL")

    def __str__(self) -> str:
        return f"{self.name} | {self.repo_url} ({self.id})"

    def get_absolute_url(self):
        """Generate URL path to project view."""
        return f"/projects/{self.id}/targets"

    @property
    def statistics(self) -> ProjectStatistics:
        """Aggregate statistics about this project's relationships."""
        module_count_aggregate = models.Count("id", distinct=True)
        test_count_aggregate = models.Count("test__id", distinct=True)
        aggregates = self.module_set.aggregate(module_count=module_count_aggregate, test_count=test_count_aggregate)
        aggregates["target_count"] = self.target_set.count()
        return ProjectStatistics(**aggregates)


class Target(TimeStampedModel):
    """Target configuration for a project."""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["projects.Target"])
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    name = models.CharField("Target Name", max_length=255)
    python_major_version = models.PositiveIntegerField(default=3)
    python_minor_version = models.PositiveIntegerField(default=7)
    python_patch_version = models.PositiveIntegerField(default=3)
    additional_details = models.TextField(
        help_text="Any further information to differentiate this target from others. (Ex. Django==2.0)",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.project.name} @ {self.name} ({self.id})"

    @property
    def full_version(self) -> str:
        """Concatenated python version and additional details as an identifier."""
        return f"{self.python_version}{'+' + self.additional_details.strip() if self.additional_details else ''}"

    @property
    def python_version(self) -> str:
        """Concatenated python version."""
        return f"{self.python_major_version}.{self.python_minor_version}.{self.python_patch_version}"


class Module(TimeStampedModel):
    """Python module which tests have been organized into."""

    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    path = models.CharField(
        "Module Path", max_length=511, help_text="Project root-relative filesystem path to test module."
    )

    class Meta:  # noqa: D106
        ordering = ("path",)

    def __str__(self) -> str:
        return self.path


class Test(TimeStampedModel):
    """Py.test routine."""

    module = models.ForeignKey("projects.Module", on_delete=models.CASCADE)
    name = models.CharField("Test Name", max_length=511, help_text="Name of test routine.")

    class Meta:  # noqa: D106
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.module.path}::{self.name}"


class Version(TimeStampedModel):
    """Version of codebase for Project at Build time."""

    hash = models.CharField("Commit Hash", unique=True, max_length=63, help_text="Git commit hash as hexadecimal.")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.hash[0:8]} by {self.author.email}"
