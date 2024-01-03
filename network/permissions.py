from rest_framework import permissions


class UserIsActive(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True
        return False


class IsUserAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return False
