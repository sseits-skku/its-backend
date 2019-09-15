from django.db import models


class FileModel(models.Model):
    file = models.FileField(verbose_name='실제 파일',
                            upload_to='files')
    token = models.CharField(verbose_name='파일 토큰',
                             max_length=255,
                             default='', blank=True)
    is_open = models.BooleanField(verbose_name='파일 열림',
                                  default=False)
    is_public = models.BooleanField(verbose_name='공개 여부')

    class Meta:
        app_label = 'mediaprovider'
        ordering = ('pk', )
        verbose_name = '파일'
        verbose_name_plural = '파일들'

    def __str__(self):
        return self.file.name
