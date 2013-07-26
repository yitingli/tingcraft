from django.conf import settings
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
    url(r'^(?P<username>[-_\w]+)/noteboard/', include('noteboards.urls', namespace='noteboard')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
