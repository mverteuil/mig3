from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField
from model_utils.models import TimeStampedModel


class Project(TimeStampedModel):
    """Project undergoing migration from a target to one or more other targets"""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["projects.Project"])
    name = models.CharField("Project Name", max_length=255)
    repo_url = models.URLField("Repository URL")


class Target(TimeStampedModel):
    """Target configuration for a project."""

    id = HashidAutoField(primary_key=True, salt=settings.HASHID_SALTS["projects.Target"])
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    name = models.CharField("Target Name", max_length=255)
    python_major_version = models.PositiveIntegerField(default=3)
    python_minor_version = models.PositiveIntegerField(default=7)
    python_patch_version = models.PositiveIntegerField(default=3)
    additional_details = models.TextField(
        help_text="Any further information to differentiate this target from others. (Ex. Django==2.0)"
    )


class Module(TimeStampedModel):
    """Python module which tests have been organized into."""

    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    path = models.CharField(
        "Module Path", max_length=511, help_text="Project root-relative filesystem path to test module."
    )


class Test(TimeStampedModel):
    """Python test routine"""

    module = models.ForeignKey("projects.Module", on_delete=models.CASCADE)
    name = models.CharField("Test Name", max_length=511, help_text="Name of test routine.")


class Version(TimeStampedModel):
    """Version of codebase for Project at Build time"""

    id = models.CharField("Version Identifier", primary_key=True, help_text="Git commit SHA-hash as hexadecimal.")
    owner = models.ForeignKey("accounts.UserAccount", on_delete=models.CASCADE)
