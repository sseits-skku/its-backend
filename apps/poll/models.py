from django.db import models
from django.utils import timezone
from polymorphic.models import PolymorphicModel


class Choice(models.Model):
    title = models.CharField(verbose_name='선택지',
                             max_length=255,
                             editable=False,
                             null=True, blank=True)
    image = models.ImageField(verbose_name='선택지 이미지',
                              max_length=255,
                              editable=False,
                              null=True, blank=True)
    created_date = models.DateTimeField(verbose_name='투표 생성일',
                                        auto_now_add=timezone.now)
    created_user = models.ForeignKey('account.User',
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True)
    poll = models.ForeignKey('BasePoll',
                             verbose_name='투표',
                             on_delete=models.CASCADE)
    selected_user = models.ManyToManyField('account.User')

    class Meta:
        app_label = 'poll'
        ordering = ('-created_date', )
        verbose_name = '선택지'
        verbose_name_plural = '선택지들'

    def __str__(self):
        return self.title


class BasePoll(PolymorphicModel):
    title = models.CharField(verbose_name='투표 제목',
                             max_length=255)
    text = models.TextField(verbose_name='투표 내용')
    watched_user = models.ManyToManyField('account.User',
                                          verbose_name='이 투표를 본 사람')
    voted_user = models.ManyToManyField('account.User',
                                        verbose_name='투표 한 사람')
    created_date = models.DateTimeField(verbose_name='투표 생성일',
                                        auto_now=timezone.now)
    modified_date = models.DateTimeField(verbose_name='투표 수정일',
                                         auto_now=timezone.now)
    start_time = models.DateTimeField(verbose_name='투표 시작시각')
    end_time = models.DateTimeField(verbose_name='투표 종료시각')

    class Meta:
        app_label = 'poll'
        ordering = ('-created_date', )
        verbose_name = '투표'
        verbose_name_plural = '투표들'

    def __str__(self):
        return self.title
