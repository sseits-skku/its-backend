from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Place, Status, OSType, Stock, ComputerStock
from .serializers import PlaceSerializer, StatusSerializer, OSTypeSerializer, StockSerializer, ComputerStockSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]


class OSTypeViewSet(ModelViewSet):
    queryset = OSType.objects.all()
    serializer_class = OSTypeSerializer
    permission_classes = [IsAuthenticated]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]


class ComputerStockViewSet(ModelViewSet):
    queryset = ComputerStock.objects.all()
    serializer_class = ComputerStockSerializer
    permission_classes = [IsAuthenticated]
