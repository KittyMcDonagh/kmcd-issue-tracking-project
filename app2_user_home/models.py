from django.db import models

# Create model for user details.

class UserDetail(models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    user_type = models.CharField(max_length=1, blank=False)
    vend_cust_id = models.IntegerField(blank=False)
    user_email_addr = models.CharField(max_length=64, blank=False)
    user_contact_nr = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.user_name
