from django.contrib import admin

from .models import MediaImage, MediaVideo


class MediaImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'image')
    search_fields = ['pk', 'owner']

admin.site.register(MediaImage, MediaImageAdmin)


class MediaVideoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'video_code')
    search_fields = ['pk', 'owner']

admin.site.register(MediaVideo, MediaVideoAdmin)
