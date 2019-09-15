from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer as ms


User = get_user_model()


class UserSerializer(ms):
    class Meta:
        model = User
        exclude = ['password', 'user_permissions']
