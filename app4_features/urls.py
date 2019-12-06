from django.conf.urls import url
from .views import features_home, feature_details, all_features_list, get_features

urlpatterns = [
    url(r'^features/$', features_home, name="features_home"),
    url(r'^features/(?P<pk>\d+)/$', feature_details, name='feature_details'),
    url(r'^features/all$', all_features_list, name="all_features_list"),
    url(r'^features/featurelist$', get_features, name="get_features"),
   
]