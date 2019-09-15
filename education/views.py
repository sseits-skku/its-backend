from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Category, Education
from .serializers import CategorySerializer, EducationSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['list', 'retrieve']:
            perm_classes = [AllowAny]
        return [perm() for perm in perm_classes]


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['list', 'retrieve']:
            perm_classes = [AllowAny]
        return [perm() for perm in perm_classes]
