from django.db import models

"""
Feature Model - This model contains all the fields that are required on the 
feature
"""

class Feature(models.Model):
    input_date = models.DateField(auto_now_add=True)
    client_code = models.CharField(max_length=6, blank=True)
    software_component = models.CharField(max_length=25, blank=True)
    user_id = models.CharField(max_length=10, blank=False)
    title = models.CharField(max_length=50, blank=True)
    summary = models.CharField(max_length=100, blank=True)
    details = models.CharField(max_length=1000, blank=True)
    paid = models.DecimalField(max_digits=6, decimal_places=2)
    status  = models.CharField(max_length=8, default="DRAFT")
    assigned_vendor_user = models.CharField(max_length=10, blank=True)
    assigned_client_user = models.CharField(max_length=10, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    thumbs_up_count = models.IntegerField(default=0)
    
    def __str__(self):
        return "{0} - {1}: {2}, {3}, {4}, {5}".format(self.id, self.client_code, self.title, self.status, self.thumbs_up_count, self.paid )
        

"""
Feature Comments Model - This model contains all the fields that are required on 
the comments entered for the feature by vendor-side and client-side users
"""
class FeatureComment(models.Model):
    feature_id = models.IntegerField(blank=False)
    input_date = models.DateField(auto_now_add=True)
    vend_client_ind = models.CharField(max_length=1, blank=False)
    vend_client_code = models.CharField(max_length=6, blank=True)
    user_id = models.CharField(max_length=10, blank=False)
    comments = models.CharField(max_length=300, blank=False)
    
    def __str__(self):
        return "{0}: {1} - {2}".format(self.vend_client_code, self.feature_id, self.user_id )


"""
Feature Paid Model - This model records the Features that a client has paid for,
the number of thumbs ups, and the amounts paid
"""

class FeaturePaid(models.Model):
    feature_id = models.IntegerField(blank=False)
    client_code = models.CharField(max_length=6, blank=True)
    author = models.CharField(max_length=6, blank=True)
    user_id = models.CharField(max_length=10, blank=False)
    thumbs_up = models.IntegerField(default=0) 
    amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return "{0}: {1} - {2}, {3}, {4}, {5}".format(self.feature_id, self.client_code, self.author, self.user_id, self.thumbs_up, self.amount_paid  )


