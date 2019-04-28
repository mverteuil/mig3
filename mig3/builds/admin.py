from django.contrib import admin

from . import models


@admin.register(models.Build)
class BuildAdmin(admin.ModelAdmin):
    readonly_fields = ("number", "version", "target", "builder")


@admin.register(models.TestOutcome)
class TestOutcomeAdmin(admin.ModelAdmin):
    readonly_fields = ("test", "result", "build")
