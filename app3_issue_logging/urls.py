from django.conf.urls import url
from app2_user_home.views import userhome
from .views import new_issue


urlpatterns = [
    url(r'^userhome/$', userhome, name="userhome"),
    url(r'^new_issue/$', new_issue, name="new_issue"),
   
]
