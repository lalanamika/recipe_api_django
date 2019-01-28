"""
object level permissions - to ensure that only the owner of a recipe
can edit / delete it.
"""

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # READ permissions are allowed to any request,
        # so we will always allow GET, HEAD, or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the recipe owner
        return obj.author == request.user
