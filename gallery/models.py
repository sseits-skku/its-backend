from django.db import models
from django.utils import timezone


class Gallery(models.Model):
    title = models.CharField(verbose_name='사진묶음 제목',
                             max_length=255)
    date = models.DateTimeField(verbose_name='사진묶음 생성일',
                                auto_now=timezone.now)
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
    image = models.ImageField(verbose_name='사진 파일',
                              upload_to='gallery')
    gallery = models.ForeignKey('Gallery',
                                verbose_name='사진묶음 분류',
                                on_delete=models.CASCADE)

    class Meta:
        app_label = 'gallery'
        ordering = ('pk', )
        verbose_name = '사진'
        verbose_name_plural = '사진들'

    def __str__(self):
        return self.image.name
