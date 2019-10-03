from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import OHTable, OHEntry
from .serializers import OHTableSerializer, OHEntrySerializer


class OHTableViewSet(ModelViewSet):
    queryset = OHTable.objects.all()
    serializer_class = OHTableSerializer
    permission_classes = [IsAuthenticated]


class OHEntryViewSet(ModelViewSet):
    queryset = OHEntry.objects.all()
    serializer_class = OHEntrySerializer
    permission_classes = [IsAuthenticated]
