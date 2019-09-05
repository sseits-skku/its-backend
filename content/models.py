from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import os
import uuid

from utils.permissions import OwnerMixin


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('media/', filename)


class Content(models.Model):
    created_date = models.DateTimeField(
        verbose_name=_('Content created date'),
        auto_now_add=timezone.now
    )
    modified_date = models.DateTimeField(
        verbose_name=_('Content modified date'),
        auto_now=timezone.now
    )
    deleted = models.BooleanField(verbose_name=_('Is deleted?'),
                                  default=False)

    class Meta:
        app_label = 'content'
        abstract = True
        ordering = ('-created_date', )
        verbose_name = _('content')

    def delete(self, *args, **kwargs):
        # Fake deletion.
        self.deleted = True
        self.save()

    def _delete(self, *args, **kwargs):
        super().delete()


class ImageContent(Content, OwnerMixin):
    image = models.ImageField(upload_to=get_file_path,
                              verbose_name=_('Image'),
                              blank=True)

    class Meta:
        app_label = 'content'
        ordering = ('-created_date', )
        verbose_name = _('image content')

    def __str__(self):
        return str(self.image.name)


class FileContent(Content, OwnerMixin):
    file = models.FileField(verbose_name=_('File'))
    caption = models.CharField(max_length=255,
                               verbose_name=_('File caption'),
                               blank=True, null=True)

    class Meta:
        app_label = 'content'
        ordering = ('-created_date', )
        verbose_name = _('file content')

    def __str__(self):
        return str(self.file.name)


class TextSnippet(Content):
    text = models.TextField(verbose_name=_('Content'),
                            blank=True)
    content_type = models.CharField(max_length=255,
                                    verbose_name=_('Content type'),
                                    default='Markdown',
                                    blank=True)

    class Meta:
        app_label = 'content'
        abstract = True
        ordering = ('-created_date', )
        verbose_name = _('text snippet')
