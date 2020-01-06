from django.conf.urls import url
from .views import features_home, feature_details, get_features, new_edit_feature, update_feature,new_feature_comment, features_report

urlpatterns = [
    url(r'^features/$', features_home, name="features_home"),
    url(r'^(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/featurehomelist/$', features_home, name="features_home_list"),
    url(r'^features/new_feature/$', new_edit_feature, name="new_feature"),
    url(r'^(?P<pk>\d+)-(?P<view_comments>[y,n])-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/$', feature_details, name='feature_details'),
    url(r'^features/(?P<pk>\d+)-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/edit/$', new_edit_feature, name='edit_feature'),
    url(r'^features/(?P<pk>\d+)-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/update/$', update_feature, name='update_feature'),
    url(r'^features/featurelist$', get_features, name="get_features"),
    url(r'^features(?P<pk>\d+)-(?P<back_to_page>\d+)-(?P<list_filters>[_,0-9A-Za-z]+)/comments/$', new_feature_comment, name='new_feature_comment'),
    url(r'^featuresreport/$', features_report, name='features_report'),
]