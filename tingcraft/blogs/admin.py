from django.contrib import admin

from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'owner')
    search_fields = ['content', 'owner']
    date_hierarchy = 'created'

admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'owner', 'blog', 'parent_comment')
    search_fields = ['content', 'owner']
    date_hierarchy = 'created'

admin.site.register(Comment, CommentAdmin)
