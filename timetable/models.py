from django.db import models
from django.utils import timezone


class OHTable(models.Model):
    semester = models.CharField(verbose_name='학기',
                                max_length=255)
    modified_date = models.DateTimeField(verbose_name='OH 시간표 수정 날짜',
                                         auto_now=timezone.now)
    json_data = models.TextField(verbose_name='OH 시간표 데이터')

    class Meta:
        app_label = 'timetable'
        ordering = ('-semester',)
        verbose_name = 'OH 시간표'
        verbose_name = 'OH 시간표들'

    def __str__(self):
        return f'{self.semester} OH 시간표'
