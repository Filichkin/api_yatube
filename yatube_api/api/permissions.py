from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Only for author allowed.'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
