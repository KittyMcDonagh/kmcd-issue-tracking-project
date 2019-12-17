from django import forms

# See class Issue in models.py - this is imported here
from .models import Issue
from .models import IssueComment

"""
Form for inputting and Editing Issues
"""

class LogNewIssueForm(forms.ModelForm):
   
    class Meta:
        model = Issue
        fields = ("client_code", "user_id", "assigned_client_user", "assigned_vendor_user", "software_component", "title", "summary", "details", "priority", "status")

"""
Form that allows updating of the Issue Status
"""
class IssueStatusForm(forms.ModelForm):
   
    class Meta:
        model = Issue
        fields = ("status",)


"""
Form that allows inputting of Issue comments
"""
class IssueCommentForm(forms.ModelForm):
   
    class Meta:
        model = IssueComment
        fields = ("issue_id", "vend_client_ind", "vend_client_code", "user_id", "comments",)
        
        



