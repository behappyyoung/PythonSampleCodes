from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('polls.urls')),

    url(r'^(?i)admin/', include(admin.site.urls)),
    url(r'^(?i)polls/', include('polls.urls', namespace="polls")),
##    url(r'^(?i)accounts/', include('userena.urls')),
)
