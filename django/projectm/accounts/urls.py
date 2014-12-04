__author__ = 'young'

from django.conf.urls import patterns, include, url
from userena import views as userena_views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    url(r'^$', login_required(userena_views.ProfileListView.as_view()), name='userena_profile_list'),
    url(r'^', include('userena.urls')),
)
