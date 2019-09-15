from django.conf import settings
from django.http import JsonResponse, FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import (
    MethodNotAllowed,
    NotAuthenticated,
    NotFound
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import FileModel
from .serializers import UploadSerializer
from .tasks import url_timeout

import json
import os
from secrets import token_urlsafe


def open_view(request):
    if request.method == 'POST':
        file_name = json.loads(request.body)['file']
        fm = get_object_or_404(FileModel, file=file_name)
        if fm.is_public or request.user.is_authenticated:
            fm.token = token_urlsafe(settings.TOKEN_LENGTH)
            fm.is_open = True
            fm.save()
            url_timeout.apply_async((fm.pk, ), countdown=settings.TOKEN_TIMEOUT)
            return JsonResponse({'success': True, 'expires_at': settings.TOKEN_TIMEOUT})
        else:
            raise NotAuthenticated()
    raise MethodNotAllowed(request.method)


def file_view(request, token):
    if request.method in ['GET', 'DELETE']:
        fm = FileModel.objects.filter(token=token)
        if not fm.exists():
            raise NotFound()
        f = fm.file.path
        if request.method == 'GET':
            return FileResponse(open(f, 'rb'))
        elif request.method == 'DELETE':
            fm.delete()
            os.unlink(f)
            return JsonResponse({'success': True})
    raise MethodNotAllowed(request.method)


class UploadViewSet(ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = UploadSerializer

    def get_permissions(self):
        perm_classes = []
        if self.action == 'create':
            perm_classes = [IsAuthenticated]
        return [perm() for perm in perm_classes]
