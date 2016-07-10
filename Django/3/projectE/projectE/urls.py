
from django.conf.urls import url
from django.contrib import admin

from shipment import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^login/$', views.user_login, name='login'),
    ##url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
