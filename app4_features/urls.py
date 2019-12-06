from django.conf.urls import url
from .views import features_home, feature_details, all_features_list, get_features, new_edit_feature, update_feature_status

urlpatterns = [
    url(r'^features/$', features_home, name="features_home"),
    url(r'^features/new_feature/$', new_edit_feature, name="new_feature"),
    url(r'^features/(?P<pk>\d+)/edit/$', new_edit_feature, name='edit_feature'),
    url(r'^features/(?P<pk>\d+)/update/$', update_feature_status, name='update_feature_status'),
    url(r'^features/(?P<pk>\d+)/$', feature_details, name='feature_details'),
    url(r'^features/all$', all_features_list, name="all_features_list"),
    url(r'^features/featurelist$', get_features, name="get_features"),
   
]