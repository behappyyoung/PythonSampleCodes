from django.conf.urls import url
from users import views

urlpatterns = [

    url(r'^(?i)profile/$', views.profile, name='user_profile'),

]