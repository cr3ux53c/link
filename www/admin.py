from django.contrib import admin
from www.models import Link


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'href')


admin.site.register(Link, LinkAdmin)
