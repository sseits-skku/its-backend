from django.contrib.auth.models import (
    AbstractUser, UserManager
)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    skku_id = models.CharField(verbose_name=_('SKKU ID'),
                               max_length=255,
                               null=True, blank=True)
    birthday = models.DateField(verbose_name=_('Birthday'),
                                null=True)
    phone_num = models.CharField(verbose_name=_('Phone number'),
                                 max_length=255,
                                 null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'account'
        ordering = ('-date_joined', )

    def delete(self, *args, **kwargs):
        # Fake deletion.
        self.is_active = False
        self.save()

    def _delete(self, *args, **kwargs):
        super().delete()
