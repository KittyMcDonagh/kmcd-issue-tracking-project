"""kmcd_issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from accounts.views import index
from accounts.views import logout

from app1_home import urls as urls_apphome
from app1_home.views import home

from app2_user_home import urls as urls_user_home
from app3_issue_logging import urls as urls_issue_logging
from app4_features import urls as urls_features

from app6_cart import urls as urls_cart
from app7_checkout import urls as urls_checkout

# Import serve

from django.views.static import serve

from django.views import static

# Import MEDIA_ROOT - this is how we're going to serve out our media URL

from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^issue_tracker/', include(urls_accounts)),
    url(r'^issue_tracker/', include(urls_apphome)),
    url(r'^issue_tracker/', include(urls_user_home)),
    url(r'^issue_tracker/', include(urls_issue_logging)),
    url(r'^feature_tracker/', include(urls_features)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
   
]
