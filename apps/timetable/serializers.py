from rest_framework.serializers import ModelSerializer

from .models import OHTable


class OHTableSerializer(ModelSerializer):
    class Meta:
        model = OHTable
        fields = '__all__'
