from celery import shared_task

from .models import FileModel


@shared_task
def url_timeout(pk):
    try:
        fm = FileModel.objects.get(pk=pk)
        fm.token = ''
        fm.is_open = False
        fm.save()
    except FileModel.DoesNotExist:
        pass
