from django.conf.urls import url
from app1_home.views import home



urlpatterns = [
    url(r'^apphome/$', home, name="home"),
   
]

