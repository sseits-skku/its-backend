from rest_framework.serializers import ModelSerializer

from .models import OHTable, OHEntry


class OHEntrySerializer(ModelSerializer):
    class Meta:
        models = OHEntry
        exclude = ['color', ]


class OHTableSerializer(ModelSerializer):
    entries = OHEntrySerializer(read_only=True, many=True)

    class Meta:
        model = OHTable
        depth = 1
        fields = '__all__'
