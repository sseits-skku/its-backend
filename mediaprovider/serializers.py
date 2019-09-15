from rest_framework.serializers import ModelSerializer

from .models import FileModel


class UploadSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        excludes = ('token', 'is_open')
