from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # only owners of an object can edit it or view it.
        return obj.name == request.user