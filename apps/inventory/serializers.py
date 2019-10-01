from rest_framework.serializers import ModelSerializer

from .models import Place, Status, OSType, Stock, ComputerStock


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class OSTypeSerializer(ModelSerializer):
    class Meta:
        model = OSType
        fields = '__all__'


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class ComputerStockSerializer(ModelSerializer):
    class Meta:
        model = ComputerStock
        fields = '__all__'
