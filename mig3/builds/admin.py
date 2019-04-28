from django.contrib import admin

from . import models


@admin.register(models.Build)
class BuildAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TestOutcome)
class TestOutcomeAdmin(admin.ModelAdmin):
    pass
