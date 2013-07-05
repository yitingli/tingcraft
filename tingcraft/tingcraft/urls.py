from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from .views import HomeView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^tingcraft/', include('tingcraft.foo.urls')),

    url(r'^accounts/login/', 'users.views.login', name='login'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
