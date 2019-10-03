from django.db import models
from django.utils import timezone

import os


class Category(models.Model):
    title = models.CharField(verbose_name='분류 이름',
                             max_length=255)

    class Meta:
        app_label = 'education'
        ordering = ('title', )
        verbose_name = '교육자료 분류'
        verbose_name_plural = '교육자료 분류들'

    def __str__(self):
        return self.title


class Education(models.Model):
    category = models.ForeignKey('Category',
                                 verbose_name='교육자료 분류',
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True)
    owner = models.ForeignKey('account.User',
                              verbose_name='교육자료 작성자',
                              on_delete=models.SET_NULL,
                              null=True)
    file = models.FileField(verbose_name='교육자료 파일',
                            upload_to='files')
    is_public = models.BooleanField(verbose_name='교육자료 공개 여부')
    caption = models.CharField(verbose_name='교육자료 설명',
                               max_length=255)
    created_date = models.DateTimeField(verbose_name='교육자료 생성일',
                                        auto_now_add=timezone.now,
                                        blank=True)
    modified_date = models.DateTimeField(verbose_name='교육자료 수정일',
                                         auto_now=timezone.now,
                                         blank=True)

    class Meta:
        app_label = 'education'
        ordering = ('-created_date',)
        verbose_name = '교육자료'
        verbose_name_plural = '교육자료들'

    def delete(self, *args, **kwargs):
        # This will remain directories
        # if you set upload_to parameter in file field.
        path = self.file.path
        super().delete(*args, **kwargs)
        os.unlink(path)

    def __str__(self):
        return f'{self.created_date}: {self.caption}'
