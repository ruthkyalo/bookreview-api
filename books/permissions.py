from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Read-only for everyone (GET, HEAD, OPTIONS).
    - Write (PUT, PATCH, DELETE) only allowed for the owner.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS (always allowed)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner
        return obj.user == request.user
