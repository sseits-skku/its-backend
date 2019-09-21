from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from .models import Apply, ApplyTerm
from .serializers import ApplySerializer, ApplyTermSerializer


class ApplyViewSet(ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['create']:
            perm_classes = [AllowAny]
        return [perm() for perm in perm_classes]


class ApplyTermViewSet(ModelViewSet):
    queryset = ApplyTerm.objects.all()
    serializer_class = ApplyTermSerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['retrieve', 'list']:
            perm_classes = [AllowAny]
        return [perm() for perm in perm_classes]
