from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Category, Education
from .serializers import CategorySerializer, EducationSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        request.data.update({'owner': request.user.pk})
        return super().create(request, *args, **kwargs)


class EducationDownloadView(APIView):
    def get(self, request, id, *args, **kwargs):
        edu = get_object_or_404(Education, pk=id)
        if edu.is_public or request.user.is_authenticated:
            res = FileResponse(open(edu.file.path, 'rb'))
            res['Content-Disposition'] = 'attachment; filename="{0}"'.format(edu.file.name.rsplit('/', 1)[1])
            return res
        return Response({'success': False}, status=HTTP_401_UNAUTHORIZED)

    def delete(self, request, id, *args, **kwargs):
        edu = get_object_or_404(Education, pk=id)
        if request.user.is_authenticated:
            edu.delete()
            return Response({'success': True})
        return Response({'success': False}, status=HTTP_401_UNAUTHORIZED)
