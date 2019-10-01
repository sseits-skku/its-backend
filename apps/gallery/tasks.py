from celery import shared_task
from PIL import Image

import os

from . import models


@shared_task
def convert_and_save(image_pk):
    try:
        i = models.Image.objects.get(pk=image_pk)
        f, e = os.path.splitext(i.image_fallback.path)
        outfile = f + '.webp'
        Image.open(f + e).save(outfile)
        i.image = outfile
        i._save()
    except Image.DoesNotExist:
        pass
