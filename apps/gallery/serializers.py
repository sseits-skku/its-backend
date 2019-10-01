from rest_framework.serializers import ModelSerializer

from .models import Gallery, Image


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
