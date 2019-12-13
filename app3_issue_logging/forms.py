from django import forms

# See class Issue in models.py - this is imported here
from .models import Issue
from .models import IssueComment

# Create a form based on forms.ModelForm (see imported forms above)

class LogNewIssueForm(forms.ModelForm):
   
    class Meta:
        model = Issue
        fields = ("client_code", "user_id", "assigned_client_user", "assigned_vendor_user", "software_component", "title", "summary", "details", "priority", "status")

class IssueStatusForm(forms.ModelForm):
   
    class Meta:
        model = Issue
        fields = ("status",)


class IssueCommentForm(forms.ModelForm):
   
    class Meta:
        model = IssueComment
        fields = ("issue_id", "vend_client_ind", "vend_client_code", "user_id", "comments",)
        
        



