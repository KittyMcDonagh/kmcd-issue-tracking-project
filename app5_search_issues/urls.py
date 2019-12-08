from django.conf.urls import url 

from .views import search_issues

urlpatterns = [
    
    url(r'^$', search_issues, name='search_issues')
    
    ]