from django.conf.urls import url
from app2_user_home.views import userhome
from app2_user_home.views import all_issues
from app2_user_home.views import our_issues_only
from app2_user_home.views import other_clients_issues_only
from app2_user_home.views import jq_issues



urlpatterns = [
    url(r'^userhome/$', userhome, name="userhome"),
    url(r'^all_issues/$', all_issues, name="all_issues"),
    url(r'^our_issues_only/$', our_issues_only, name="our_issues_only"),
    url(r'^other_clients_issues_only/$', other_clients_issues_only, name="other_clients_issues_only"),
    url(r'^jq_issues/$', jq_issues, name="jq_issues"),
   
]
