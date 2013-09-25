# core/api.py
from django.conf.urls import patterns, url

from noteboards.views import NoteCreateAPIView


urlpatterns = patterns('',

    url(r'^noteboard/note/create/$', NoteCreateAPIView.as_view(), name='noteboard-note-create'),

)
