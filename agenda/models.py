from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from content.models import TextSnippet
from utils.permissions import OwnerMixin


User = get_user_model()


class Label(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name=_("Label name"),
                             null=False, blank=False, unique=True)
    ccode = models.CharField(max_length=255,
                             verbose_name=_("Label color code"),
                             default="#888888")

    class Meta:
        app_label = 'agenda'
        ordering = ('title', )
        verbose_name = _('label')

    def __str__(self):
        return self.title


class Agenda(OwnerMixin):
    title = models.CharField(max_length=255,
                             verbose_name=_("Agenda title"),
                             null=False, blank=False)
    labels = models.ManyToManyField('Label',
                                    verbose_name=_('Label'),
                                    blank=True)
    assignee = models.ManyToManyField(User,
                                      verbose_name=_('Assignee'),
                                      related_name="assignee",
                                      blank=True)
    is_closed = models.BooleanField(verbose_name=_("Is closed?"),
                                    default=False)
    created_date = models.DateTimeField(verbose_name=_("Agenda created date"),
                                        auto_now_add=timezone.now)
    modified_date = models.DateTimeField(verbose_name=_("Agenda created date"),
                                         auto_now=timezone.now)

    class Meta:
        app_label = 'agenda'
        ordering = ('id', )
        verbose_name = _('agenda')
    
    def __str__(self):
        return self.title


class Action(OwnerMixin, TextSnippet):
    agenda = models.ForeignKey('Agenda',
                               verbose_name=_("Agenda"),
                               on_delete=models.CASCADE)
    action_type = models.CharField(max_length=255,
                                   verbose_name=_("Action name"),
                                   null=False, blank=False)

    class Meta:
        app_label = 'agenda'
        ordering = ('created_date', )
        verbose_name = _('action')

    def __str__(self):
        return self.text
