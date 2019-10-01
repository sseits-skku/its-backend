from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import OHTable
from .serializers import OHTableSerializer


class OHTableViewSet(ModelViewSet):
    queryset = OHTable.objects.all()
    serializer_class = OHTableSerializer
    permission_classes = [IsAuthenticated]
