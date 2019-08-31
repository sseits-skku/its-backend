from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class IPAddress(models.Model):
    pub_date = models.DateTimeField(verbose_name=_('IP published date.'),
                                    auto_now=timezone.now)
    ip_addr = models.GenericIPAddressField(verbose_name=_('IP Address'),
                                           null=True, blank=True)

    class Meta:
        app_label = 'iptable'
        verbose_name = _('IP Address')
        verbose_name_plural = _('IP Addresses')

    def __str__(self):
        return self.ip_addr
