from rest_framework.serializers import (
    Serializer, ModelSerializer,
    CharField, ValidationError
)

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'groups']
