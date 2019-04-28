from django.contrib import admin

from . import models


@admin.register(models.BuilderAccount)
class BuilderAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    pass
