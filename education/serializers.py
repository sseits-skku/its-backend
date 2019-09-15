from rest_framework.serializers import ModelSerializer

from .models import Category, Education


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
