from rest_framework.serializers import ModelSerializer as ms
from .models import Computer, OSType, Stock, \
                    StockStatus, StockType


class StockStatusSerializer(ms):
    class Meta:
        model = StockStatus
        fields = '__all__'


class StockTypeSerializer(ms):
    class Meta:
        model = StockType
        fields = '__all__'


class OSTypeSerializer(ms):
    class Meta:
        model = OSType
        fields = '__all__'


class StockSerializer(ms):
    class Meta:
        model = Stock
        fields = '__all__'


class ComputerSerializer(ms):
    class Meta:
        model = Computer
        fields = '__all__'
