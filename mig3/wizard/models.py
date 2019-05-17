from django.contrib.auth import get_user_model
from django.db import models
from django.utils.decorators import classproperty

from accounts import models as accounts
from builds import models as builds
from projects import models as projects


class SetupProgressStagesMeta:
    """Attach STAGES property to SetupProgress based on the order the stages are defined in the class."""

    def __new__(cls, name, bases, dct):
        """Build class with STAGES defined."""
        new_class = type(name, bases, dct)
        new_class.STAGES = [stage_name for stage_name, property in dct.items() if isinstance(property, classproperty)]
        return new_class


class SetupProgress(metaclass=SetupProgressStagesMeta):
    """Determine how much progress has been made in setting up the mig3 configuration."""

    @classproperty
    def has_administrator(self) -> bool:
        """Has at least one active administrator."""
        return get_user_model().objects.filter(is_active=True, is_superuser=True).exists()

    @classproperty
    def has_builder(self) -> bool:
        """Has at least one Builder Account."""
        return accounts.BuilderAccount.objects.exists()

    @classproperty
    def has_project(self) -> bool:
        """Has at least one project."""
        return projects.Project.objects.exists()

    @classproperty
    def has_targets(self) -> bool:
        """Has a project with at least two targets.

        Two or more targets are expected to be present:
            - one for the present configuration
            - at least one for desired configuration once the migration has completed

        """
        projects_with_target_counts = projects.Project.objects.annotate(target_count=models.Count("target"))
        return projects_with_target_counts.filter(target_count__gte=2).exists()

    @classproperty
    def has_builds(self) -> bool:
        """Has a build for each target."""
        return builds.Build.objects.distinct("target").count() >= 2

    @classproperty
    def has_working_installation(self) -> bool:
        """All setup progress stages are complete."""
        return all(getattr(self, stage) for stage in self.STAGES if stage != "has_working_installation")

    @classmethod
    def get_current_stage_index(cls) -> int:
        """Get the index for the current setup step."""
        for index, stage in enumerate(cls.STAGES):
            if not getattr(cls, stage):
                return index
        else:
            return len(cls.STAGES) - 1
