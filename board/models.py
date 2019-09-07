from django.db import models
from django.utils.translation import ugettext_lazy as _

from content.models import TextSnippet
from utils.permissions import OwnerMixin


class Category(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Category name',
                             unique=True, null=False, blank=False)
    member_only = models.BooleanField(verbose_name=_('Is member-only?'),
                                      default=True)

    class Meta:
        app_label = 'board'
        ordering = ('title', )
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Tag name',
                             unique=True, null=False, blank=False)

    class Meta:
        app_label = 'board'
        ordering = ('title', )
        verbose_name = _('tag')

    def __str__(self):
        return self.title


class PostStatus(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Post status',
                             unique=True, null=False, blank=False)
    detail = models.CharField(max_length=255,
                              verbose_name='Post detail',
                              null=False, blank=False)

    class Meta:
        app_label = 'board'
        ordering = ('title', )
        verbose_name = _('post status')
        verbose_name_plural = _('post statuses')

    def __str__(self):
        return self.title


class Comment(OwnerMixin, TextSnippet):
    # content from TextSnippet
    # password from AnonymousUser
    summary = models.CharField(verbose_name=_('Comment summary'),
                               max_length=255,
                               default='')
    ip_addr = models.GenericIPAddressField(verbose_name=_('Wrote IP Address'))
    deleted = models.BooleanField(verbose_name=_('Is deleted'),
                                  default=False)
    # nickname from AnonymousUser
    is_subcomment = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='subcomment',
                               on_delete=models.CASCADE)

    class Meta:
        app_label = 'board'
        ordering = ('-created_date', )
        verbose_name = _('comment')

    def __str__(self):
        return self.summary

    def delete(self, *args, **kwargs):
        # Fake deletion.
        self.deleted = True
        self.save()

    def _delete(self, *args, **kwargs):
        super().delete()


class Post(OwnerMixin, TextSnippet):
    title = models.CharField(max_length=255,
                             verbose_name='Post title',
                             null=False, blank=False)
    # content from TextSnippet
    ip_addr = models.GenericIPAddressField(verbose_name=_('Wrote IP Address'))
    deleted = models.BooleanField(verbose_name=_('Is deleted'),
                                  default=False)
    status = models.ForeignKey('PostStatus',
                               verbose_name=_('Post status'),
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    category = models.ForeignKey('Category',
                                 verbose_name=_('Post category'),
                                 on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag',
                                  verbose_name=_('Post Tags'),
                                  related_name='tag',
                                  blank=True)
    comments = models.ManyToManyField('Comment',
                                      verbose_name=_('Post comments'),
                                      related_name='comment',
                                      blank=True)
    images = models.ManyToManyField('content.ImageContent',
                                    verbose_name=_('Post images'),
                                    related_name='post_images',
                                    blank=True)
    files = models.ManyToManyField('content.FileContent',
                                   verbose_name=_('Post files'),
                                   related_name='post_files',
                                   blank=True)

    class Meta:
        app_label = 'board'
        ordering = ('-created_date', )
        verbose_name = _('post')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Fake deletion.
        self.deleted = True
        self.save()

    def _delete(self, *args, **kwargs):
        super().delete()
