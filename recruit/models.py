from django.db import models
from django.utils import timezone


class ApplyTerm(models.Model):
    start_date = models.DateField(verbose_name='모집 시작일')
    end_date = models.DateField(verbose_name='모집 종료일')
    start_interview = models.DateField(verbose_name='면접 시작일')
    end_interview = models.DateField(verbose_name='면접 종료일')

    class Meta:
        app_label = 'recruit'
        ordering = ('-start_date',)
        verbose_name = '모집 기간'

    def __str__(self):
        return f'{self.start_date}~{self.end_date}/{self.start_interview}~{self.end_interview}'


class Apply(models.Model):
    fullname = models.CharField(verbose_name='작성자',
                                max_length=255)
    skku_id = models.CharField(verbose_name='성균관대 학번',
                               max_length=255)
    phone_num = models.CharField(verbose_name='작성자 전화번호',
                                 max_length=255)
    p_skill = models.IntegerField(verbose_name='프로그래밍 실력')
    g_skill = models.IntegerField(verbose_name='게임 실력')
    h_skill = models.IntegerField(verbose_name='관계 형성 능력')
    v_skill = models.IntegerField(verbose_name='미적감각')

    created_date = models.DateTimeField(verbose_name='지원서 제출시각',
                                        auto_now_add=timezone.now,
                                        blank=True)
    interview_date = models.DateTimeField(verbose_name='면접 희망시각')
    term = models.ForeignKey('ApplyTerm',
                             on_delete=models.CASCADE)

    class Meta:
        app_label = 'recruit'
        ordering = ('-created_date',)
        verbose_name = '지원서'

    def __str__(self):
        return f'{self.interview_date}: {self.fullname}'
