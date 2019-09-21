from rest_framework.serializers import ModelSerializer

from .models import Apply, ApplyTerm


class ApplySerializer(ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'


class ApplyTermSerializer(ModelSerializer):
    class Meta:
        model = ApplyTerm
        fields = '__all__'
