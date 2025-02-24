from rest_framework import permissions

class IsAuthorOrViewOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # only owners of an object are allowed to edit it
        return obj.author == request.user
