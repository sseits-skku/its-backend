from django.shortcuts import get_object_or_404
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Gallery, Image
from .serializers import GallerySerializer, ImageSerializer


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated]


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageDownloadView(APIView):
    def get(self, request, id, *args, **kwargs):
        if request.user.is_authenticated:
            im = get_object_or_404(Image, pk=id)
            if im:
                res = FileResponse(open(im.image.path, 'rb'))
                res['Content-Disposition'] = 'attachment; filename="{0}"'.format(im.image.name.rsplit('/', 1)[1])
            else:
                res = FileResponse(open(im.image_fallback.path, 'rb'))
                res['Content-Disposition'] = 'attachment; filename="{0}"'.format(im.image_fallback.name.rsplit('/', 1)[1])
            return res
        return Response({'success': False}, status=HTTP_401_UNAUTHORIZED)
