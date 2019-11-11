from django.db import models

# Vendor Model - owner of Issue Tracking System.

class Vendor(models.Model):
    vend_code = models.CharField(max_length=6, blank=False)
    vend_name = models.CharField(max_length=50, blank=False)
    vend_address = models.CharField(max_length=100, blank=False)
    vend_city = models.CharField(max_length=30, blank=False)
    vend_country = models.CharField(max_length=30, blank=False)
    vend_email_addr = models.CharField(max_length=64, blank=False)
    vend_contact_nr = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.vend_name
        
"""
Client Model - clients that use the Accounting System for which the 
Issue Tracking System tracks issues
"""

class Client(models.Model):
    client_code = models.CharField(max_length=6, blank=False)
    client_name = models.CharField(max_length=50, blank=False)
    client_address = models.CharField(max_length=100, blank=False)
    client_city = models.CharField(max_length=30, blank=False)
    client_country = models.CharField(max_length=30, blank=False)
    user_email_addr = models.CharField(max_length=64, blank=False)
    user_contact_nr = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.client_name
        
"""
User Model - This model tells us about the user's relationship with the 
Issue Tracking System. 
The user may be working for either the Vendor or a Client of the Vendor.
The User Type indicates which - 'V'=Vendor; 'C'=Client
"""

class UserDetail(models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    user_type = models.CharField(max_length=1, blank=False)
    vend_client_code = models.CharField(max_length=6, blank=True)
    user_email_addr = models.CharField(max_length=64, blank=False)
    user_contact_nr = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.user_name
        
"""
Create a filter list for users that work for the Vendor, by which to filter 
the Issues
"""

class FilterForVendUser(models.Model):
    filter_vend_desc = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return FilterForVendUser.filter_vend_desc

"""
Create a filter list for users that work for a Client, by which to filter 
the Issues
"""

class FilterForClientUser(models.Model):
    filter_client_desc = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return FilterForClientUser.filter_client_desc

"""
Create a Status filter , by which to filter the Issues
"""

class StatusFilter(models.Model):
    status_desc = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return StatusFilter.status_desc



        