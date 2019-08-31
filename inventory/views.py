from rest_framework.viewsets import ModelViewSet as mvs

from .models import Computer, OSType, Stock,       \
                    StockStatus, StockType
from .serializers import (
    StockStatusSerializer, StockTypeSerializer, StockSerializer,
    OSTypeSerializer, ComputerSerializer
)
from utils.permissions import IsAdminUser


class StockStatusViewSet(mvs):
    queryset = StockStatus.objects.all()
    serializer_class = StockStatusSerializer
    permission_classes = [IsAdminUser]


class StockTypeViewSet(mvs):
    queryset = StockType.objects.all()
    serializer_class = StockTypeSerializer
    permission_classes = [IsAdminUser]


class StockViewSet(mvs):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminUser]


class OSTypeViewSet(mvs):
    queryset = OSType.objects.all()
    serializer_class = OSTypeSerializer
    permission_classes = [IsAdminUser]


class ComputerViewSet(mvs):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    permission_classes = [IsAdminUser]
