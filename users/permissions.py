from rest_framework.permissions import BasePermission


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
