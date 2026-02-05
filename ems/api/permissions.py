from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrManager(BasePermission):

    def has_permission(self, request, view):

        # Read-only allowed for all logged-in users
        if request.method in SAFE_METHODS:
            return True

        # Write allowed for superuser
        if request.user.is_superuser:
            return True

        # Write allowed for managers
        return request.user.groups.filter(name='Manager').exists()