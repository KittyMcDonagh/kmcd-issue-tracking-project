from django.db import models

"""
Issue Model - This model contains all the fields that are required on the 
issue
"""

class Issue(models.Model):
    input_date = models.DateTimeField(auto_now_add=True)
    client_code = models.CharField(max_length=6, blank=True)
    user_name = models.CharField(max_length=50, blank=False)
    assigned_client_user = models.CharField(max_length=50, blank=False)
    assigned_vendor_user = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=50, blank=False)
    summary = models.CharField(max_length=100, blank=False)
    details = models.CharField(max_length=500, blank=False)
    details = models.CharField(max_length=500, blank=False)
    priority = models.IntegerField(default=0)
    status  = models.CharField(max_length=8, default="DRAFT")
    progress = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.client_code
        return "{0}-{1}-{2}".format(self.input_date, self.user_name, self.client_code)
        

# Comments Model - Comments input on an issue by a Vendor-side user

class VendorComment(models.Model):
    issue_id = models.IntegerField(default=0)
    input_date = models.DateTimeField(auto_now_add=True)
    vend_client_ind = models.CharField(max_length=1, blank=False)
    vend_client_code = models.CharField(max_length=6, blank=True)
    user_name = models.CharField(max_length=50, blank=False)
    comments = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return "{0}-{1}".format(self.user_name, self.issue_id)



"""
Create a filter list for users that work for the Vendor, by which to filter 
the Issues
"""

class FilterForVendor(models.Model):
    filter_value = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.filter_value

"""
Create a filter list for users that work for a Client, by which to filter 
the Issues
"""

class FilterForClient(models.Model):
    filter_value = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.filter_value

"""
Create a Status filter , by which to filter the Issues
"""

class StatusFilter(models.Model):
    status_desc = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.status_desc

