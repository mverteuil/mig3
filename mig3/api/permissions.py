from rest_framework import permissions

from accounts import models as accounts


class IsBuilder(permissions.BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.auth, accounts.BuilderAccount)

    def has_object_permission(self, request, view, obj):
        return isinstance(request.auth, accounts.BuilderAccount)
