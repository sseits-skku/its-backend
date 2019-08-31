from rest_framework.viewsets import ModelViewSet as mvs

from .models import IPAddress
from .serializers import IPAddressSerializer
from utils.permissions import IsAdminUser


class IPAddressViewSet(mvs):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer
    permission_classes = [IsAdminUser]
