from django.db import models
from django.utils import timezone

import os

from . import tasks


def gallery_path(instance, filename):
    f, _ = os.path.splitext(filename)
    return f'images/%Y/%m/{f}/{filename}'


class Gallery(models.Model):
    title = models.CharField(verbose_name='사진묶음 제목',
                             max_length=255)
    date = models.DateTimeField(verbose_name='사진묶음 생성일',
                                auto_now=timezone.now,
                                blank=True)
    rep_img = models.OneToOneField('Image',
                                   verbose_name='대표 사진',
                                   on_delete=models.PROTECT,
                                   related_name='rep_img')

    class Meta:
        app_label = 'gallery'
        ordering = ('-date',)
        verbose_name = '사진묶음'
        verbose_name_plural = '갤러리 사진묶음들'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.FileField(verbose_name='사진 파일 WEBP',
                             blank=True, null=True)
    image_fallback = models.ImageField(verbose_name='사진 파일 (fallback)',
                                       upload_to=gallery_path)
    gallery = models.ForeignKey('Gallery',
                                verbose_name='사진묶음 분류',
                                on_delete=models.SET_NULL,
                                null=True, blank=True)

    class Meta:
        app_label = 'gallery'
        ordering = ('pk',)
        verbose_name = '사진'
        verbose_name_plural = '사진들'

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        tasks.convert_and_save.delay(self.pk)

    def delete(self, *args, **kwargs):
        # This will remain directories
        # if you set upload_to parameter in file field.
        im = self.image.path
        imf = self.image_fallback.path
        super(Image, self).delete(*args, **kwargs)
        os.unlink(im)
        os.unlink(imf)

    def _save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.image.name
