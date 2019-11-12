from django.conf.urls import url
from app1_home.views import home
from app1_home.views import registered


urlpatterns = [
    url(r'^apphome/$', home, name="home"),
    url(r'^apphomereg/$', registered, name="registered"),
   
]

