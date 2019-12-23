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
    assigned_client_user = models.CharField(max_length=10, blank=False)
    assigned_vendor_user = models.CharField(max_length=10, blank=False)
    title = models.CharField(max_length=50, blank=True)
    summary = models.CharField(max_length=100, blank=True)
    details = models.CharField(max_length=700, blank=True)
    priority = models.IntegerField(default=5)
    status  = models.CharField(max_length=8, default="DRAFT")
    thumbs_up_count = models.IntegerField(default=0) 
    
    def __str__(self):
        return "{0} - {1}: {2}, {3}, {4}, {5}".format(self.id, self.client_code, self.assigned_client_user, self.title, self.status, self.thumbs_up_count )
        

"""
Issue Comments Model - This model contains all the fields that are required on 
the comments entered for the issue by vendor-side and client-side users
"""

class IssueComment(models.Model):
    issue_id = models.IntegerField(blank=False)
    input_date = models.DateField(auto_now_add=True)
    vend_client_ind = models.CharField(max_length=1, blank=False)
    vend_client_code = models.CharField(max_length=6, blank=True)
    user_id = models.CharField(max_length=10, blank=False)
    comments = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return "{0}: {1} - {2}".format(self.vend_client_code, self.issue_id, self.user_id )


"""
Issue Thumbs Up Model - This model records the Issues that a client has 
'thumbed up'. They can only have one 'thumbs up' per issue. 
Once thumbed up, The icon for the issue will change to 'thumb down', and once 
clicked, this will change the count back to zero.
"""

class IssueThumbsUp(models.Model):
    issue_id = models.IntegerField(blank=False)
    client_code = models.CharField(max_length=6, blank=True)
    author = models.CharField(max_length=6, blank=True)
    user_id = models.CharField(max_length=10, blank=False)
    thumbs_up = models.IntegerField(default=0) 
    
    def __str__(self):
        return "{0}: {1} - {2}, {3}, {4}".format(self.issue_id, self.client_code, self.user_id, self.author, self.thumbs_up )
        
        