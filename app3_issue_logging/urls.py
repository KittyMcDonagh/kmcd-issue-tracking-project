from django.conf.urls import url
from .views import new_edit_issue, issue_details, update_issue_status, new_issue_comment

urlpatterns = [
    url(r'^new_issue/$', new_edit_issue, name="new_issue"),
    url(r'^(?P<pk>\d+)/$', issue_details, name='issue_details'),
    url(r'^(?P<pk>\d+)/edit/$', new_edit_issue, name='edit_issue'),
    url(r'^(?P<pk>\d+)/update/$', update_issue_status, name='update_issue_status'),
    url(r'^(?P<pk>\d+)/comments/$', new_issue_comment, name='new_issue_comment'),
]
