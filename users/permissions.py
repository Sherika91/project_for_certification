from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """ Custom permission to only allow owners of an object to edit it. """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.is_admin:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    """ Custom permission to only allow admins to access. """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
