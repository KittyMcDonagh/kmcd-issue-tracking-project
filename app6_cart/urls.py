# Code copied from the e-commerce lesson

from django.conf.urls import url
from .views import view_cart, add_to_cart, add_to_cart_js, adjust_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^add_js/', add_to_cart_js, name='add_to_cart_js'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    
]
    