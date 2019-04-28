from django.contrib import admin

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Target)
class TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    pass
