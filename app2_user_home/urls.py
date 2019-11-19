from django.conf.urls import url
from app2_user_home.views import userhome
from .views import get_issues


urlpatterns = [
    url(r'^userhome/$', userhome, name="userhome"),
    url(r'^get_issues/$', get_issues, name="get_issues"),
   
]
