from django.conf.urls import url
from .views import user_home
from .views import get_issues, iss_thumbs_up_down

"""
URLs for the Home Page, User Home Page, Get Issues from the DB, Process 'Thumbs Up' / 'Thumbs Down'
"""

urlpatterns = [
    url(r'^userhome/$', user_home, name="user_home"),
    url(r'^(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/userhomelist/$', user_home, name="user_home_list"),
    url(r'^userhome/issueslist/$', get_issues, name="get_issues"),
    url(r'^userhome/issueslist/thumbs/$', iss_thumbs_up_down, name="iss_thumbs_up_down"),
]
