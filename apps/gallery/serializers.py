from rest_framework.serializers import ModelSerializer

from .models import Gallery, Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class GallerySerializer(ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Gallery
        depth = 1
        fields = '__all__'
