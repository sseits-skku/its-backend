from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserSerializer, GroupSerializer, PermissionSerializer
)
from utils.permissions import IsStaffUser, IsOwner

User = get_user_model()


class UserViewSet(mvs):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['create', 'destroy']:
            perm_classes = [IsStaffUser]
        elif self.action in ['update', 'partial_update']:
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
