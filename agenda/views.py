from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)

from .models import Action, Label, Agenda
from .serializers import (
    ActionSerializer,
    LabelSerializer,
    AgendaSerializer
)
from utils.permissions import (
    IsOwner, IsStaffUser
)
from utils.viewsets import OwnerModelViewSet as omvs


class ActionViewSet(omvs):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    def get_permissions(self):
        perm_classes = [IsStaffUser]
        if self.action in ['update', 'partial_update']:
            perm_classes = [IsOwner]
        elif self.action in ['create', 'list', 'retrieve']:
            perm_classes = [IsAuthenticated]
        return [perm() for perm in perm_classes]


class AgendaViewSet(omvs):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['delete']:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]


class LabelViewSet(mvs):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def get_permissions(self):
        perm_classes = [IsAuthenticated]
        if self.action in ['delete']:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
