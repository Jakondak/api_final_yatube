from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        safe_method = request.method in permissions.SAFE_METHODS
        auth_user = request.user.is_authenticated
        return safe_method or auth_user

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or \
               obj.author == request.user
