
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
