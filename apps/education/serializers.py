from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Category, Education


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EducationSerializer(ModelSerializer):
    file_url = SerializerMethodField()

    class Meta:
        model = Education
        exclude = ['file']

    def get_file_url(self, obj):
        # TODO: 배포를 위해서 고쳐야 함.
        return f'http://localhost:8000/edu/download/{obj.pk}'
