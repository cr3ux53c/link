from django.db import models


# Create your models here.

class Link(models.Model):
    class Meta:
        verbose_name = '링크'
        verbose_name_plural = '링크'

    href = models.URLField(verbose_name='링크')
    name = models.CharField(verbose_name='이름', max_length=200, blank=True, null=True)
    path = models.CharField(verbose_name='단축 경로', max_length=50, unique=True, blank=True, null=True)
