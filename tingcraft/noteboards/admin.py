from django.contrib import admin

from .models import NoteBoard, Note, NoteComment


class NoteBoardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'owner', 'rank')
    search_fields = ['title', 'owner']
    date_hierarchy = 'created'

admin.site.register(NoteBoard, NoteBoardAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'board', 'content')
    search_fields = ['content']
    date_hierarchy = 'created'

admin.site.register(Note, NoteAdmin)


class NoteCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'owner', 'note', 'parent_comment')
    search_fields = ['content', 'owner']
    date_hierarchy = 'created'

admin.site.register(NoteComment, NoteCommentAdmin)
