from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@api_view(http_method_names=['POST'])
def login_view(request, *args, **kwargs):
    u = request.data.get('username', '')
    p = request.data.get('password', '')
    user = authenticate(username=u, password=p)
    if user and user.is_active:
        request.session.set_expiry(86400)
        login(request, user)
        return Response({'username': user.username, 'userId': user.pk, 'isAdmin': user.is_superuser})
    return Response({}, status=HTTP_404_NOT_FOUND)


@api_view(http_method_names=['POST'])
def logout_view(request, *args, **kwargs):
    logout(request)
    return Response({})


@api_view(http_method_names=['GET'])
def user_view(request):
    user = None
    print(request.user)
    if request.user.is_authenticated:
        user = request.user
        return Response({'username': user.username, 'userId': user.pk, 'isAdmin': user.is_superuser})
    return Response({}, status=HTTP_401_UNAUTHORIZED)
