from django.conf import settings
from django.http import JsonResponse, FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import (
    api_view,
    authentication_classes
)
from rest_framework.exceptions import (
    MethodNotAllowed,
    NotAuthenticated,
    NotFound
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import FileModel
from .serializers import UploadSerializer
from .tasks import url_timeout

import json
import os
from secrets import token_urlsafe


@api_view(['POST'])
@authentication_classes((JWTAuthentication,))
def open_view(request):
    try:
        file_id = json.loads(request.body)['file_id']
    except KeyError:
        raise NotFound()
    fm = get_object_or_404(FileModel, id=file_id)
    if fm.is_public or request.user.is_authenticated:
        fm.token = token_urlsafe(settings.TOKEN_LENGTH)
        fm.is_open = True
        fm.save()
        url_timeout.apply_async((fm.pk, ), countdown=settings.TOKEN_TIMEOUT)
        return JsonResponse({
            'success': True,
            'token': fm.token,
            'expires_at': settings.TOKEN_TIMEOUT
        })
    else:
        raise NotAuthenticated()


@api_view(['GET', 'DELETE'])
def file_view(request, token):
    if request.method in ['GET', 'DELETE']:
        fm = get_object_or_404(FileModel, token=token)
        f = fm.file.path
        if request.method == 'GET':
            res = FileResponse(open(f, 'rb'))
            res['Content-Disposition'] = 'attachment; filename="{0}"'.format(fm.file.name.rsplit('/', 1)[1])
            return res
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
