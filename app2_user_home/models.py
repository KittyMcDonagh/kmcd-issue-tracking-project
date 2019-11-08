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
        

# Customer Model - Customers that use the Accounting System for which the 
# Issue Tracking System tracks issues

class Customer(models.Model):
    cust_code = models.CharField(max_length=6, blank=False)
    cust_name = models.CharField(max_length=50, blank=False)
    cust_address = models.CharField(max_length=100, blank=False)
    cust_city = models.CharField(max_length=30, blank=False)
    cust_country = models.CharField(max_length=30, blank=False)
    user_email_addr = models.CharField(max_length=64, blank=False)
    user_contact_nr = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.cust_name
        
# User Model - The user may be working for the Vendor or for the Customer.
# The User Type indicates which - 'V'=Vendor; 'C'=Customer

class UserDetail(models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    user_type = models.CharField(max_length=1, blank=False)
    vend_cust_code = models.CharField(max_length=6, blank=True)
    user_email_addr = models.CharField(max_length=64, blank=False)
    user_contact_nr = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.user_name
        