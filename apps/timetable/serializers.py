from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import OHTable, OHEntry


class OHEntrySerializer(ModelSerializer):
    ohtable = SlugRelatedField(slug_field='semester', read_only=True)

    class Meta:
        model = OHEntry
        depth = 1
        fields = ['id', 'name', 'start', 'end', 'color', 'ohtable']


class OHTableSerializer(ModelSerializer):
    entries = OHEntrySerializer(read_only=True, many=True)

    class Meta:
        model = OHTable
        depth = 1
        fields = '__all__'
