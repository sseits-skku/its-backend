from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from utils.permissions import IsStaffUser, IsOwner

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['create', 'destroy']:
            perm_classes = [IsStaffUser]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        return [perm() for perm in perm_classes]
