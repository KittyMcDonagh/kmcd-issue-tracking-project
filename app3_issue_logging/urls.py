from django.conf.urls import url
from .views import new_issue, issue_detail

urlpatterns = [
    url(r'^new_issue/$', new_issue, name="new_issue"),
    url(r'^(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
   
]
