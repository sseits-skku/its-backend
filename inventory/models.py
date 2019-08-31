from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from content.models import TextSnippet
from utils.placeholder_models import SharedCharField, PlaceholderModel


class StockStatus(PlaceholderModel):
    title = SharedCharField(vname='Stock status',
                            null=False,
                            unique=True)

    class Meta(PlaceholderModel.Meta):
        app_label = 'inventory'
        ordering = ('title', )
        verbose_name = _('stock status')
        verbose_name_plural = _('stock statuses')


class StockType(PlaceholderModel):
    title = SharedCharField(vname='Stock type',
                            null=False,
                            unique=True)

    class Meta(PlaceholderModel.Meta):
        app_label = 'inventory'
        ordering = ('title', )
        verbose_name = _('stock type')


class OSType(models.Model):
    major = SharedCharField(vname='OS type',
                            null=False)
    version = SharedCharField(vname='OS version',
                              null=True, blank=True)
    edition = SharedCharField(vname='OS edition',
                              null=True, blank=True)
    bit = SharedCharField(vname='OS bit',
                          null=False)

    class Meta(PlaceholderModel.Meta):
        app_label = 'inventory'
        ordering = ('major', 'version', 'bit')
        verbose_name = _('OS type')
        
    def __str__(self):
        return f"{self.major} {self.version} {self.edition} {self.bit}bit"


class Stock(TextSnippet):
    stock_id = SharedCharField(vname='Stock ID',
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
    model_name = SharedCharField(vname='Computer model name',
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
