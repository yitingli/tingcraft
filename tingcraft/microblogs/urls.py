from django.conf.urls import patterns, include, url

from .views import MicroBlogListView, MicroBlogCreateView


urlpatterns = patterns('',

    url(r'^$', MicroBlogListView.as_view(), name='list'),
    url(r'^create/$', MicroBlogCreateView.as_view(), name='create'),

)
