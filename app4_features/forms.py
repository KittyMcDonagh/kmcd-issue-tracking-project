from django import forms

# See class Feaure in models.py - this is imported here

from .models import Feature, FeatureComment

# Create a form based on forms.ModelForm (see imported forms above)

class LogNewFeatureForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("client_code", "user_id", "assigned_client_user", "assigned_vendor_user", "software_component", "title", "summary", "details", "paid", "status", "price")

class FeatureStatusForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("status",)

# This form is used to update the amount paid for a feature, when a payment is 
# successfully made

class FeatureAmountPaidForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("paid",)



"""
Form that allows inputting of Feature comments
"""
class FeatureCommentForm(forms.ModelForm):
   
    class Meta:
        model = FeatureComment
        fields = ("feature_id", "vend_client_ind", "vend_client_code", "user_id", "comments",)
        
