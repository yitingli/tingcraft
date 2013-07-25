from django.contrib import admin

from .models import MicroBlog, MicroComment


class MicroBlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'owner')
    search_fields = ['content', 'owner']
    date_hierarchy = 'created'

admin.site.register(MicroBlog, MicroBlogAdmin)


class MicroCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'owner', 'micro_blog', 'parent_comment')
    search_fields = ['content', 'owner']
    date_hierarchy = 'created'

admin.site.register(MicroComment, MicroCommentAdmin)
