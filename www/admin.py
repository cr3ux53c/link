from django.contrib import admin
from www.models import Link, Metadata


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'href')
    fields = ['href', 'path', 'name']


admin.site.register(Link, LinkAdmin)
admin.site.register(Metadata)
