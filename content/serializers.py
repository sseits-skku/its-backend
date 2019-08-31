from .models import FileContent, ImageContent
from rest_framework.serializers import HyperlinkedModelSerializer as hms, \
                                       ModelSerializer as ms, FileField,  \
                                       ImageField


class ImageContentSerializer(hms):
    image = ImageField(use_url=True)

    class Meta:
        model = ImageContent
        fields = ('image', )


class FileContentSerializer(hms):
    file = FileField(use_url=True)

    class Meta:
        model = FileContent
        fields = ('file', 'caption', )
