from django.conf.urls import url
from app2_user_home.views import userhome
from app2_user_home.views import all_issues
from app2_user_home.views import our_issues_only
from app2_user_home.views import other_clients_issues_only
from app2_user_home.views import jq_get_issues


urlpatterns = [
    url(r'^userhome/$', userhome, name="userhome"),
    url(r'^jq_get_issues/$', jq_get_issues, name="jq_get_issues"),
   
]
