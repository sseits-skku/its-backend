from django.contrib.auth.models import (
    AbstractUser, UserManager
)
from django.db import models


class User(AbstractUser):
    skku_id = models.CharField(verbose_name='SKKU ID',
                               max_length=255,
                               null=True, blank=True)
    birthday = models.DateField(verbose_name='생년월일',
                                null=True)
    phone_num = models.CharField(verbose_name='전화번호',
                                 max_length=255,
                                 null=True, blank=True)
    nickname = models.CharField(verbose_name='닉네임',
                                max_length=255,
                                blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'account'
        ordering = ('-date_joined', )
        verbose_name = '계정'
        verbose_name_plural = '계정들'

    def delete(self, *args, **kwargs):
        # Fake deletion.
        self.is_active = False
        self.save()

    def _delete(self, *args, **kwargs):
        super().delete()
