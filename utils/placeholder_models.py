from django.db import models
from django.utils.translation import ugettext_lazy as _


class SharedCharField(models.CharField):
    def __init__(self, vname=None, vnames=None, *args, **kwargs):
        if vname:
            kwargs['verbose_name'] = _(vname)
        if not kwargs.get('max_length'):
            kwargs['max_length'] = 255
        super().__init__(*args, **kwargs)


class PlaceholderModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.title
