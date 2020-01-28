from django import forms

# See class Feaure in models.py - this is imported here

from .models import Feature, FeatureComment

# This form allows input / edit of Features

class LogNewFeatureForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("client_code", "user_id", "assigned_client_user", "assigned_vendor_user", "software_component", "title", "summary", "details", "paid", "status", "price", "image")


# This allows the Status, Price, Assigned Vendor User, and Assigned Client User fields on a Feature to be updated

class UpdateFeatureForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("status", "price", "assigned_vendor_user", "assigned_client_user")


# This form is used to update the amount paid for a feature, when a payment is 
# successfully made

class FeatureAmountPaidForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("paid",)


"""
This Form allows input of Feature comments
"""
class FeatureCommentForm(forms.ModelForm):
   
    class Meta:
        model = FeatureComment
        fields = ("feature_id", "vend_client_ind", "vend_client_code", "user_id", "comments",)
        
