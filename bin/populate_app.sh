#!/usr/bin/env python3
import django
from django.apps import apps

import sys
import os

serializer_header = '''from rest_framework.serializers import ModelSerializer

from .models import {0}
'''
serializer_template = '''

class {0}Serializer(ModelSerializer):
    class Meta:
        model = {0}
        fields = '__all__'
'''
viewset_header = '''from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import {0}
from .serializers import {1}
'''
viewset_template = '''

class {0}ViewSet(ModelViewSet):
    queryset = {0}.objects.all()
    serializer_class = {0}Serializer
    permission_classes = [IsAuthenticated]
'''
urls_header = '''from django.urls import path, include
from rest_framework import routers

from .views import {0}

router = routers.DefaultRouter()
'''
urls_template = '''router.register('{0}', {1})
'''
urls_footer = '''
urlpatterns = [
    path('', include(router.urls))
]
'''
admin_header = '''from django.contrib import admin

from .models import {0}
'''
admin_template = '''

@admin.register({0})
class {0}Admin(admin.ModelAdmin):
    pass
'''

if __name__ == '__main__':
    sys.path.append(".")
    django.setup()

    app_label = sys.argv[1]
    app_path = os.path.abspath(os.path.join(__file__, '..', app_label))
    serializer_path = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'apps',
            app_label,
            'serializers.py'
        )
    )
    view_path = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'apps',
            app_label,
            'views.py'
        )
    )
    urls_path = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'apps',
            app_label,
            'urls.py'
        )
    )
    admin_path = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'apps',
            app_label,
            'admin.py'
        )
    )
    model_list = [*map(lambda x: x.__name__, apps.all_models[app_label].values())]

    if len(model_list) == 0:
        print(f'No models detected in {app_label} app.')
        exit(1)

    with open(serializer_path, 'w') as f:
        f.write(serializer_header.format(', '.join(model_list)))
        for m in model_list:
            f.write(serializer_template.format(m))

    with open(view_path, 'w') as f:
        f.write(viewset_header.format(
            ', '.join(model_list),
            ', '.join(map(lambda x: x + 'Serializer', model_list))
        ))
        for m in model_list:
            f.write(viewset_template.format(m))

    with open(urls_path, 'w') as f:
        f.write(urls_header.format(
            ', '.join(map(lambda x: x + 'ViewSet', model_list))
        ))
        for m in model_list:
            f.write(urls_template.format(
                m.lower(),
                m + 'ViewSet'
            ))
        f.write(urls_footer)

    with open(admin_path, 'w') as f:
        f.write(admin_header.format(', '.join(model_list)))
        for m in model_list:
            f.write(admin_template.format(m))

    print(f'Populate \'{app_label}\' app successfully.')
