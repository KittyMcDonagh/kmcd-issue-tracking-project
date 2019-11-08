from django.conf.urls import url
from app2_user_home.views import userhome



urlpatterns = [
    url(r'^userhome/$', userhome, name="userhome"),
   
]

