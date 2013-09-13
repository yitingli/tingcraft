from django.db import models
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import ExpDevision, ExpItem


class ExpDevisionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'owner', 'rank')
    search_fields = ['pk', 'name', 'owner']
    date_hierarchy = 'created'

admin.site.register(ExpDevision, ExpDevisionAdmin)


class ExpItemAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
    list_display = ('pk', 'title', 'position', 'place', 'content')
    search_fields = ['pk', 'title']
    date_hierarchy = 'created'

admin.site.register(ExpItem, ExpItemAdmin)
