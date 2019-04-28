from django.contrib import admin

from . import models


@admin.register(models.BuilderAccount)
class BuilderAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("email", "name", "id")}),
        ("Rank", {"fields": ("is_staff", "is_superuser")}),
        ("Timestamps", {"classes": ("collapse",), "fields": ("created", "modified", "last_login")}),
        ("Permissions", {"classes": ("collapse",), "fields": ("user_permissions", "groups")}),
    )
    readonly_fields = ("id", "email", "created", "modified", "last_login")
