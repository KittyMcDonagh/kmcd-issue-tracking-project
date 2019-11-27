from django.conf.urls import url
from .views import user_home
from .views import get_issues


urlpatterns = [
    url(r'^userhome/$', user_home, name="user_home"),
    url(r'^userhome/issueslist/$', get_issues, name="get_issues"),
   
]
