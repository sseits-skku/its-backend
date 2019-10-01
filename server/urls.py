from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from apps.account.views import login_view, logout_view

ADMIN_URL = 'admin/'
if hasattr(settings, 'ADMIN_URL'):
    ADMIN_URL = settings.ADMIN_URL

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('account/', include('apps.account.urls')),
    path('edu/', include('apps.education.urls')),
    path('finance/', include('apps.finance.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('inventory/', include('apps.inventory.urls')),
    # path('poll/', include('apps.poll.urls')),
    path('recruit/', include('apps.recruit.urls')),
    path('timetable/', include('apps.timetable.urls')),
    path(ADMIN_URL, admin.site.urls)
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('api-auth/', include('rest_framework.urls',
                                  namespace='rest_framework')),
        path('__debug__', include(debug_toolbar.urls)),
    ]
