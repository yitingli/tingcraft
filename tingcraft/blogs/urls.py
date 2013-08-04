from django.conf.urls import patterns, include, url

from .views import BlogListView, BlogCreateView


urlpatterns = patterns('',

    url(r'^$', BlogListView.as_view(), name='list'),
    url(r'^create/$', BlogCreateView.as_view(), name='create'),

)
