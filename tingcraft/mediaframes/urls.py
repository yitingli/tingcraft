from django.conf.urls import patterns, include, url

from .views import MediaFrameCreateView


urlpatterns = patterns('',

    url(r'^create/$', MediaFrameCreateView.as_view(), name='create'),

)
