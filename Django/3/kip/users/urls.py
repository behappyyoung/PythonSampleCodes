from django.conf.urls import url
from users import views

urlpatterns = [

    url(r'^$', views.users_list, name='user_list'),
    url(r'^profile/$', views.profile, name='user_profile'),

]