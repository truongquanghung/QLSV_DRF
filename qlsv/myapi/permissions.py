from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return request.user.is_superuser

from django.http import Http404

class CustomPermission(object):

    def has_permissions(self):
        # Assumes that your Article model has a foreign key called `auteur`.
        return self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404('You do not have permission.')
            
        return super(CustomPermission, self).dispatch(
            request, *args, **kwargs)