import abc
from typing import Union

from django.contrib.auth import get_user_model
from django.db import models

from accounts import models as accounts
from builds import models as builds
from projects import models as projects


class RequirementChecker(abc.ABC):
    """Discrete requirements stage of installation setup."""

    condition_name: str = None

    @staticmethod
    @abc.abstractmethod
    def check() -> bool:
        """Check if this requirement is met."""
        return NotImplemented


class HasAdministrator(RequirementChecker):
    """Has at least one active administrator."""

    condition_name = "Active Administrator Account"

    @staticmethod
    def check() -> bool:
        """Check if this requirement is met."""
        return get_user_model().objects.filter(is_active=True, is_superuser=True).exists()


class HasBuilder(RequirementChecker):
    """Has at least one Builder Account."""

    condition_name = "Builder Account"

    @staticmethod
    def check() -> bool:
        """Check if this requirement is met."""
        return accounts.BuilderAccount.objects.exists()


class HasProject(RequirementChecker):
    """Has at least one project."""

    condition_name = "First Project"

    @staticmethod
    def check() -> bool:
        """Check if this requirement is met."""
        return projects.Project.objects.exists()


class HasTargets(RequirementChecker):
    """Has a project with at least two targets.

    Two or more targets are expected to be present:
        - one for the present configuration
        - at least one for desired configuration once the migration has completed

    """

    condition_name = "Source and Destination Targets"

    @staticmethod
    def check() -> bool:
        """Check if this requirement is met."""
        projects_with_target_counts = projects.Project.objects.annotate(target_count=models.Count("target"))
        return projects_with_target_counts.filter(target_count__gte=2).exists()


class HasBuilds(RequirementChecker):
    """Has a build for each target."""

    condition_name = "One Build for Each Target"

    @staticmethod
    def check() -> bool:
        """Check if this requirement is met."""
        return builds.Build.objects.distinct("target").count() >= 2


class InstallationSetup:
    """Determine how much progress has been made in setting up the mig3 installation."""

    #: Conditions which must be met before installation setup is considered complete.
    REQUIREMENTS: list = [HasAdministrator, HasBuilder, HasProject, HasTargets, HasBuilds]

    @classmethod
    def is_complete(cls) -> bool:
        """All installation setup requirements have been met."""
        return all(requirement.check() for requirement in cls.REQUIREMENTS)

    @classmethod
    def get_current_requirement_index(cls) -> Union[int, None]:
        """Get the index for the current setup step."""
        for index, requirement in enumerate(cls.REQUIREMENTS):
            if not requirement.check():
                return index
        return None
