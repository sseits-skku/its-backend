from celery import shared_task
from celery.utils.log import get_task_logger

from . import models
from utils.random import color_gen


logger = get_task_logger('server')


@shared_task
def set_color(id):
    entries = models.OHEntry.objects.filter(ohtable=id)
    names = [e.name for e in entries.only('name')]
    colors = color_gen(len(names))
    for i in range(len(names)):
        for e in models.OHEntry.objects.filter(name=names[i]):
            e.color = colors[i]
            e._save()
