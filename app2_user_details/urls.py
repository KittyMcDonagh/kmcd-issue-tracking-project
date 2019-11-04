from django.conf.urls import url
from app2_user_details.views import userpage



urlpatterns = [
    url(r'^userdetails/$', userpage, name="userpage"),
   
]

