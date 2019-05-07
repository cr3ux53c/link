from django.db import models


# Create your models here.

class Metadata(models.Model):
    class Meta:
        verbose_name = '단축 링크 접두 URL'
        verbose_name_plural = '단축 링크 접두 URL'

    prefix = models.URLField(verbose_name='단축 링크 접두 URL', unique=True)

    def __str__(self):
        return self.prefix


class Link(models.Model):
    class Meta:
        verbose_name = '링크'
        verbose_name_plural = '링크'

    href = models.URLField(verbose_name='링크')
    path = models.CharField(verbose_name='단축 경로', max_length=50)
    name = models.CharField(verbose_name='이름', max_length=200, blank=True, null=True)
    protocol = models.CharField(verbose_name='프로토콜', max_length=20)
