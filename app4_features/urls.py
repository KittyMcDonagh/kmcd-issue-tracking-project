from django.conf.urls import url
from .views import features_home, feature_details, get_features, new_edit_feature, update_feature_status_price,new_feature_comment

urlpatterns = [
    url(r'^features/$', features_home, name="features_home"),
    url(r'^features/new_feature/$', new_edit_feature, name="new_feature"),
    url(r'^features/(?P<pk>\d+)-(?P<view_comments>[y,n])/$', feature_details, name='feature_details'),
    url(r'^features/(?P<pk>\d+)/edit/$', new_edit_feature, name='edit_feature'),
    url(r'^features/(?P<pk>\d+)/update/$', update_feature_status_price, name='update_feature_status_price'),
    url(r'^features/featurelist$', get_features, name="get_features"),
    url(r'^features(?P<pk>\d+)/comments/$', new_feature_comment, name='new_feature_comment'),
]