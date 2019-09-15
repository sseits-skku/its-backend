from django.db import models
from django.utils import timezone


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
    file = models.OneToOneField('mediaprovider.FileModel',
                                verbose_name='업로드한 자료',
                                on_delete=models.CASCADE)
    caption = models.CharField(verbose_name='교육자료 설명',
                               max_length=255)
    created_date = models.DateTimeField(verbose_name='교육자료 생성일',
                                        auto_now_add=timezone.now)
    modified_date = models.DateTimeField(verbose_name='교육자료 수정일',
                                         auto_now=timezone.now)

    class Meta:
        app_label = 'education'
        ordering = ('-created_date',)
        verbose_name = '교육자료'
        verbose_name_plural = '교육자료들'

    def __str__(self):
        return f'{self.created_date}: {self.caption}'
