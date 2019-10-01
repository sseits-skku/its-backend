from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ApplyTerm, Apply
from .serializers import ApplyTermSerializer, ApplySerializer


class ApplyTermViewSet(ModelViewSet):
    queryset = ApplyTerm.objects.all()
    serializer_class = ApplyTermSerializer
    permission_classes = [IsAuthenticated]


class ApplyViewSet(ModelViewSet):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    permission_classes = [IsAuthenticated]
