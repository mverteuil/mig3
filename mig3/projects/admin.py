from django.contrib import admin

from builds import models as builds
from . import models


class TargetInline(admin.TabularInline):
    model = models.Target
    extra = 0


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TargetInline]


class TestInline(admin.StackedInline):
    model = models.Test
    extra = 0


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [TestInline]


class BuildInline(admin.TabularInline):
    model = builds.Build
    extra = 0
    classes = ("collapse",)
    fields = ("number", "target", "builder")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    inlines = [BuildInline]
    readonly_fields = ("id", "author")
