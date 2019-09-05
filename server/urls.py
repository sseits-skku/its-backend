from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', include('account.urls')),
    path('agenda/', include('agenda.urls')),
    path('board/', include('board.urls')),
    path('inventory/', include('inventory.urls')),
    path('ip-table/', include('iptable.urls')),
    path('content/', include('content.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.contrib import admin
    import debug_toolbar

    urlpatterns += [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls',
                                  namespace='rest_framework')),
        path('__debug__', include(debug_toolbar.urls)),
    ]
