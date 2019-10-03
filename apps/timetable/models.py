from django.db import models
from django.utils import timezone

from utils.random import color_gen


class OHTable(models.Model):
    semester = models.CharField(verbose_name='학기',
                                max_length=255)

    class Meta:
        app_label = 'timetable'
        ordering = ('-semester',)
        verbose_name = 'OH 시간표'
        verbose_name_plural = 'OH 시간표들'

    def __str__(self):
        return f'{self.semester} OH 시간표'


class OHEntry(models.Model):
    ohtable = models.ForeignKey('OHTable',
                                verbose_name='OH 시간표',
                                on_delete=models.CASCADE)
    name = models.CharField(verbose_name='OH 담당자 이름',
                            max_length=255)
    start = models.CharField(verbose_name='OH 엔트리 시작 시간',
                             max_length=255)
    end = models.CharField(verbose_name='OH 엔트리 끝 시간',
                           max_length=255)
    color = models.CharField(verbose_name='OH 담당자 컬러',
                             max_length=255,
                             blank=True, null=True)

    class Meta:
        app_label = 'timetable'
        ordering = ('start',)
        verbose_name = 'OH 엔트리'
        verbose_name_plural = 'OH 엔트리들'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        entries = OHEntry.objects.filter(ohtable=self.ohtable).only('name').order_by('name')
        names = [e.name for e in entries.distinct('name')]
        colors = color_gen(len(names))
        for i in range(len(names)):
            for e in OHEntry.objects.filter(name=names[i]):
                e.color = colors[i]
                e._save()

    def _save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}: {self.start} - {self.end}'
