from rest_framework.viewsets import ModelViewSet

from .models import Transaction
from .serializers import TransactionSerializer
from utils.permissions import IsAdminUser


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminUser]
