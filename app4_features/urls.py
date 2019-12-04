from django.conf.urls import url
from .views import features_list

urlpatterns = [
    url(r'^featureslist/$', features_list, name="features_list"),
   
]