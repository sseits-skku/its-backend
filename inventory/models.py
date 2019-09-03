from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from content.models import TextSnippet


class StockStatus(models.Model):
    title = models.CharField(verbose_name='Stock status',
                             null=False, unique=True)

    class Meta:
        app_label = 'inventory'
        ordering = ('title', )
        verbose_name = _('stock status')
        verbose_name_plural = _('stock statuses')

    def __str__(self):
        return self.title


class StockType(models.Model):
    title = models.CharField(verbose_name='Stock type',
                             null=False, unique=True)

    class Meta:
        app_label = 'inventory'
        ordering = ('title', )
        verbose_name = _('stock type')

    def __str__(self):
        return self.title


class OSType(models.Model):
    major = models.CharField(verbose_name='OS type',
                             null=False)
    version = models.CharField(verbose_name='OS version',
                               null=True, blank=True)
    edition = models.CharField(verbose_name='OS edition',
                               null=True, blank=True)
    bit = models.CharField(verbose_name='OS bit',
                           null=False)

    class Meta:
        app_label = 'inventory'
        ordering = ('major', 'version', 'bit')
        verbose_name = _('OS type')

    def __str__(self):
        return f"{self.major} {self.version} {self.edition} {self.bit}bit"


class Stock(TextSnippet):
    stock_id = models.CharField(verbose_name='Stock ID',
                                null=False)
    stock_type = models.ForeignKey('StockType',
                                   verbose_name=_('Stock type'),
                                   on_delete=models.PROTECT)
    stock_status = models.ForeignKey('StockStatus',
                                     verbose_name=_('Stock status'),
                                     on_delete=models.PROTECT)
    added_date = models.DateTimeField(verbose_name=_('Added Date'),
                                      auto_now_add=timezone.now)

    class Meta:
        app_label = 'inventory'
        ordering = ('stock_id', )
        verbose_name = _('stock')

    def __str__(self):
        return self.stock_id


class Computer(Stock):
    model_name = models.CharField(verbose_name='Computer model name',
                                  null=False)
    os = models.ForeignKey('OSType',
                           verbose_name=_('Installed OS Type'),
                           on_delete=models.SET_NULL,
                           null=True, blank=True)
    ip_addr = models.ForeignKey('iptable.IPAddress',
                                verbose_name=_('Allocated IP Address'),
                                on_delete=models.SET_NULL,
                                null=True, blank=True)

    class Meta:
        app_label = 'inventory'
        ordering = ('stock_id', )
        verbose_name = _('computer')
