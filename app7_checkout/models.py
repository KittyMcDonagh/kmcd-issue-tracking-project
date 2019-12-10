# NOTE: These were copied from the ecommerce project and adjusted

from django.db import models

from app4_features.models import Feature

class Order(models.Model):    
       
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.id, self.full_name)


class OrderLineItem(models.Model):
    
    # Although not in the video, "on_delete=models.CASCADE," needs to be 
    # added to 'ForeignKey' otherwise you get a red x
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)    
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.feature.title, self.feature.price)
        