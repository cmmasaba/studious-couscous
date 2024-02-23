from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # only owners of an object are allowed to edit it
        return obj.owner == request.user
