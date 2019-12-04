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
    paid = models.IntegerField(default=5)
    status  = models.CharField(max_length=8, default="DRAFT")
    
    def __str__(self):
        return "{0} - {1}: {2}, {3}, {4}".format(self.id, self.client_code, self.user_id, self.title, self.status )
        

