from django.conf.urls import patterns, include, url

from .views import BlogListView, BlogCreateView, BlogDetailView


urlpatterns = patterns('',

    url(r'^$', BlogListView.as_view(), name='list'),
    url(r'^create/$', BlogCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/', BlogDetailView.as_view(), name='detail'),

)
