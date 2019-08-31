from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework.permissions import AllowAny

from .serializers import (
    UserSerializer, GroupSerializer, PermissionSerializer
)
from utils.permissions import IsStaffUser, IsOwner

User = get_user_model()


class UserViewSet(mvs):
    queryset = User.objects                  \
                   .order_by('-date_joined') \
                   .all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            perm_classes = [IsStaffUser]
        elif self.action in ['create']:
            perm_classes = [AllowAny]
        else:
            perm_classes = [IsOwner]
        return [perm() for perm in perm_classes]


class GroupViewSet(mvs):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_permissions(self):
        perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class PermissionViewSet(mvs):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def get_permissions(self):
        perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
