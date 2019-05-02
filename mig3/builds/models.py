import django_fsm
from django.db import models
from django_choices_enum import ChoicesEnum
from model_utils.models import TimeStampedModel


class BuildManager(models.Manager):
    use_for_related_fields = True
    use_in_migrations = True

    def create_build(self, number, target, version, builder, results):
        build = self.model(number=number, target=target, version=version, builder=builder)
        build.save()
        for test_result in results:
            module, _ = target.project.module_set.get_or_create(path=test_result["test__module__path"])
            test, _ = module.test_set.get_or_create(name=test_result["test__name"])
            build.testoutcome_set.update_or_create(test=test, result=test_result["result"])
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


class TestOutcome(TimeStampedModel):
    """Test outcome accepted because it moved the migration state forward."""

    class Results(int, ChoicesEnum):
        ERROR = (0, "Error")
        FAILED = (1, "Failed")
        PASSED = (2, "Passed")
        SKIPPED = (3, "Skipped")
        XFAILED = (4, "XFailed")

        @classmethod
        def exclude(cls, *excluded):
            return [member for member in cls if member not in excluded]

    build = models.ForeignKey("builds.Build", on_delete=models.CASCADE)
    test = models.ForeignKey("projects.Test", on_delete=models.CASCADE)
    result = django_fsm.FSMIntegerField(choices=Results.choices(), default=Results.ERROR)

    def __str__(self):
        return f"{self.test}: {self.Results(self.result).name.lower()} as of {self.build}"

    @django_fsm.transition("result", source=[Results.ERROR, Results.FAILED], target=Results.XFAILED)
    def set_xfailed(self):
        pass

    @django_fsm.transition("result", source=Results.exclude(Results.PASSED), target=Results.PASSED)
    def set_passed(self):
        pass
