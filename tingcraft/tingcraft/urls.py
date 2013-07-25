from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from .views import HomeView, UserHomeView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^accounts/', include('users.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<username>[-_\w]+)/$', UserHomeView.as_view(), name='user_home'),
    url(r'^(?P<username>[-_\w]+)/microblog/', include('microblogs.urls', namespace='microblog')),

)
