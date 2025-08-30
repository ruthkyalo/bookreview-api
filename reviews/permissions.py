from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - SAFE methods (GET, HEAD, OPTIONS) → allowed for anyone
    - Write methods (POST, PUT, PATCH, DELETE) → only allowed for the owner of the review
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the review's owner
        return obj.user == request.user
