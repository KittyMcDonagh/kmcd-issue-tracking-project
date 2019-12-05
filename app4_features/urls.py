from django.conf.urls import url
from .views import my_features_list, feature_details, all_features_list

urlpatterns = [
    url(r'^featureslist/$', my_features_list, name="my_features_list"),
    url(r'^(?P<pk>\d+)/$', feature_details, name='feature_details'),
    url(r'^userhome/all/$', all_features_list, name="all_features_list"),
   
]