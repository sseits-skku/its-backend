from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from .models import Category, Education


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EducationSerializer(ModelSerializer):
    owner = SerializerMethodField('get_owner_name')

    class Meta:
        model = Education
        fields = '__all__'

    def get_owner_name(self, obj):
        return f"{obj.owner.last_name}{obj.owner.first_name}"   \
            if obj.owner.nickname == '' else obj.owner.nickname
