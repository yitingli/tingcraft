from django.conf.urls import patterns, include, url

from .views import UserCreateView, UserUpdateView, UserPasswordChangeView


urlpatterns = patterns('',

    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^register/$', UserCreateView.as_view(), name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'users/logged_out.html', 'next_page': '/'},
        name='logout'),
    url(r'^update/$', UserUpdateView.as_view(), name='user_update'),
    url(r'^password/change$', UserPasswordChangeView.as_view(), name='user_password_change'),

)
