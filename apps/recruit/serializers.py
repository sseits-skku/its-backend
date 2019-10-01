from rest_framework.serializers import ModelSerializer

from .models import ApplyTerm, Apply


class ApplyTermSerializer(ModelSerializer):
    class Meta:
        model = ApplyTerm
        fields = '__all__'


class ApplySerializer(ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'
