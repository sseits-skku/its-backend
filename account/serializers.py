from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework.serializers import ModelSerializer as ms


User = get_user_model()


class UserSerializer(ms):
    class Meta:
        model = User
        exclude = ['password', 'user_permissions']


class GroupSerializer(ms):
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSerializer(ms):
    class Meta:
        model = Permission
        fields = '__all__'
