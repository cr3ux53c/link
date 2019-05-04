from django.db import models


# Create your models here.

class Link(models.Model):
    class Meta:
        verbose_name = '링크'
        verbose_name_plural = '링크'

    href = models.URLField()
    text = models.CharField(max_length=200)

    def __str__(self):
        tail = ''
        if len(self.href) > 50:
            tail = '...'
        return self.text + ' :: ' + self.href[:50] + tail

