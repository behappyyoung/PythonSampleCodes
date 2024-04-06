from django.urls import re_path
from info import views

urlpatterns = [

    re_path(r'^$(?i)', views.contents_list, name='contents_list'),
    re_path(r'Contents/$(?i)', views.contents_list, name='contents_list'),
    re_path(r'Content/add/$(?i)', views.add_content, name='add_content'),
    re_path(r'^Categories/$(?i)', views.categories, name='categories'),
    re_path(r'^Categories/add/$(?i)', views.add_category, name='add_category'),

    ]
