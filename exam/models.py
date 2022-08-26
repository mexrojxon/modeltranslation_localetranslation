from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class ExamModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    main_image = models.ImageField(upload_to='post-img/', verbose_name=_('main image'))

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'