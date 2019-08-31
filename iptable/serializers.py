from rest_framework.serializers import ModelSerializer as ms

from .models import IPAddress


class IPAddressSerializer(ms):
    class Meta:
        model = IPAddress
        fields = '__all__'
