from rest_framework import permissions

from accounts import models as accounts


class IsBuilder(permissions.BasePermission):
    """Require request to be authenticated using BuilderAccounts only (UserAccount not allowed)."""

    def has_permission(self, request, view):
        """Check if BuilderAccount in request in order to perform this action."""
        return isinstance(request.auth, accounts.BuilderAccount)

    def has_object_permission(self, request, view, obj):
        """Check if BuilderAccount in request in order to perform this action on this object."""
        return isinstance(request.auth, accounts.BuilderAccount)
