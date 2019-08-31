from django.db import models
from rest_framework.permissions import BasePermission

from account.models import User


class OwnerMixin(models.Model):
    owner = models.ForeignKey('account.User',
                              on_delete=models.SET_NULL,
                              null=True, blank=True)

    class Meta:
        abstract = True


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Because request has TokenUser, not User...
        # We should provide from this information.
        try:
            u = User.objects.get(pk=request.user.pk)
            return bool(u.is_authenticated and
                        u == obj.owner)
        except User.DoesNotExist:
            return False
        except AttributeError:
            return bool(u.is_authenticated and
                        u.pk == obj.pk)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        # Because request has TokenUser, not User...
        # We should provide from this information.
        try:
            u = User.objects.get(pk=request.user.pk)
            return bool(u.is_staff and
                        u.is_superuser)
        except User.DoesNotExist:
            return False


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        # Because request has TokenUser, not User...
        # We should provide from this information.
        try:
            u = User.objects.get(pk=request.user.pk)
            return bool(u.is_staff)
        except User.DoesNotExist:
            return False
