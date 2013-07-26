from django.conf.urls import patterns, include, url

from .views import NoteBoardListView, NoteListView


urlpatterns = patterns('',

    url(r'^$', NoteBoardListView.as_view(), name='list'),
    url(r'^(?P<slug>[-_\w]+)/$', NoteListView.as_view(), name='board_notes'),

)
