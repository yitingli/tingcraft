from django.conf.urls import patterns, include, url

from .views import MediaFrameCreateView, MediaFrameDetailView


urlpatterns = patterns('',

    url(r'^create/$', MediaFrameCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', MediaFrameDetailView.as_view(), name='detail'),

)
