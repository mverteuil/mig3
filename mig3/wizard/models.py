from django.contrib.auth import get_user_model
from django.db import models

from accounts import models as accounts
from builds import models as builds
from projects import models as projects


class SetupProgressStagesMeta:
    """Attach STAGES property to SetupProgress based on the order the stages are defined in the class."""

    def __new__(cls, name, bases, dct):
        """Build class with STAGES defined."""
        dct["STAGES"] = [
            name
            for name, prop in dct.items()
            if name.startswith("has_") and isinstance(prop, (classmethod, staticmethod))
        ]
        return type(name, bases, dct)


class SetupProgress(metaclass=SetupProgressStagesMeta):
    """Determine how much progress has been made in setting up the mig3 configuration."""

    #: Declared progress stages, populated by SetupProgressStagesMeta
    STAGES: list = []

    @staticmethod
    def has_administrator() -> bool:
        """Has at least one active administrator."""
        return get_user_model().objects.filter(is_active=True, is_superuser=True).exists()

    @staticmethod
    def has_builder() -> bool:
        """Has at least one Builder Account."""
        return accounts.BuilderAccount.objects.exists()

    @staticmethod
    def has_project() -> bool:
        """Has at least one project."""
        return projects.Project.objects.exists()

    @staticmethod
    def has_targets() -> bool:
        """Has a project with at least two targets.

        Two or more targets are expected to be present:
            - one for the present configuration
            - at least one for desired configuration once the migration has completed

        """
        projects_with_target_counts = projects.Project.objects.annotate(target_count=models.Count("target"))
        return projects_with_target_counts.filter(target_count__gte=2).exists()

    @staticmethod
    def has_builds() -> bool:
        """Has a build for each target."""
        return builds.Build.objects.distinct("target").count() >= 2

    @classmethod
    def has_working_installation(cls) -> bool:
        """All setup progress stages are complete."""
        return all(getattr(cls, stage)() for stage in cls.STAGES if stage != "has_working_installation")

    @classmethod
    def get_current_stage_index(cls) -> int:
        """Get the index for the current setup step."""
        for index, check_stage_complete_method_name in enumerate(cls.STAGES):
            check_stage_complete = getattr(cls, check_stage_complete_method_name)
            if not check_stage_complete():
                current_stage_index = index
                break
        else:
            current_stage_index = len(cls.STAGES) - 1
        return current_stage_index
