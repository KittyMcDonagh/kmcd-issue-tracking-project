from django.db import models

"""
Issue Model - This model contains all the fields that are required on the 
issue
"""

class Issue(models.Model):
    input_date = models.DateField(auto_now_add=True)
    client_code = models.CharField(max_length=6, blank=True)
    software_component = models.CharField(max_length=25, blank=True)
    user_id = models.CharField(max_length=10, blank=False)
    assigned_client_user = models.CharField(max_length=50, blank=False)
    assigned_vendor_user = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=50, blank=True)
    summary = models.CharField(max_length=100, blank=True)
    details = models.CharField(max_length=700, blank=True)
    priority = models.IntegerField(default=5)
    status  = models.CharField(max_length=8, default="DRAFT")
    progress = models.CharField(max_length=100, default="Initial Input")
    
    def __str__(self):
        return "{0} - {1}: {2}, {3}".format(self.client_code, self.user_id, self.title, self.status )
        

# Comments Model - Comments input on an issue by a Vendor-side user

class Comment(models.Model):
    issue_id = models.IntegerField(blank=False)
    input_date = models.DateField(auto_now_add=True)
    vend_client_ind = models.CharField(max_length=1, blank=False)
    vend_client_code = models.CharField(max_length=6, blank=True)
    user_id = models.CharField(max_length=10, blank=False)
    comments = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return "{0}: {1} - {2}".format(self.vend_client_code, self.issue_id, self.user_id )




























































































































