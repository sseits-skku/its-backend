from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', include('account.urls')),
    path('edu/', include('education.urls')),
    path('finance/', include('finance.urls')),
    path('gallery/', include('gallery.urls')),
    path('inventory/', include('inventory.urls')),
    path('media/', include('mediaprovider.urls')),
    path('recruit/', include('recruit.urls')),
    path('timetable/', include('timetable.urls')),
    # path('vote/', include('vote.urls')),
]

if settings.DEBUG:
    from django.contrib import admin
    import debug_toolbar

    urlpatterns += [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls',
                                  namespace='rest_framework')),
        path('__debug__', include(debug_toolbar.urls)),
    ]
