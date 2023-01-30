from django.urls import re_path
from info import views

urlpatterns = [

    re_path(r'^$', views.contents_list, name='contents_list'),
    re_path(r'Contents^$', views.contents_list, name='contents_list'),
    re_path(r'^Content/add/$', views.add_content, name='add_content'),

    re_path(r'^Categories/$', views.category_list, name='category_list'),

    ]
