from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)

from .models import FileContent, ImageContent
from .serializers import FileContentSerializer, ImageContentSerializer
from account.models import User
from utils.permissions import (
    IsOwner, IsStaffUser
)


class ImageContentViewSet(mvs):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer

    def get_attribute(self, instance):
        try:
            u = User.objects.get(pk=self.context['request'].user.pk).is_staff
        except User.DoesNotExist:
            u = False
        if not instance.member_only or u:
            return super(ImageContentViewSet, self).get_attribute(instance)
        return None

    def get_permissions(self):
        if self.action in ['retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:  # destroy, list
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class FileContentViewSet(mvs):
    queryset = FileContent.objects.all()
    serializer_class = FileContentSerializer

    def get_attribute(self, instance):
        try:
            u = User.objects.get(pk=self.context['request'].user.pk).is_staff
        except User.DoesNotExist:
            u = False
        if not instance.member_only or u:
            return super(FileContentViewSet, self).get_attribute(instance)
        return None

    def get_permissions(self):
        if self.action in ['retrieve']:
            perm_classes = [AllowAny]
        elif self.action in ['create']:
            perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        else:  # destroy, list
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
