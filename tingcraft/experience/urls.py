from django.conf.urls import patterns, include, url

from .views import ExpListView


urlpatterns = patterns('',

    url(r'^$', ExpListView.as_view(), name='list'),

)
