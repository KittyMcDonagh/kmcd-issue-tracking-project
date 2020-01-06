from django.conf.urls import url
from .views import new_edit_issue, issue_details, update_issue, new_issue_comment, issues_report

urlpatterns = [
    url(r'^new_issue/$', new_edit_issue, name="new_issue"),
    url(r'^(?P<pk>\d+)-(?P<view_comments>[y,n])-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/$', issue_details, name='issue_details'),
    url(r'^(?P<pk>\d+)-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/edit/$', new_edit_issue, name='edit_issue'),
    url(r'^(?P<pk>\d+)-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/update/$', update_issue, name='update_issue'),
    url(r'^(?P<pk>\d+)-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/comments/$', new_issue_comment, name='new_issue_comment'),
    url(r'^issuesreport/$', issues_report, name='issues_report'),
]
