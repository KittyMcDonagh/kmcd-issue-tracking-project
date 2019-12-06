from django import forms

# See class Feaure in models.py - this is imported here

from .models import Feature

# Create a form based on forms.ModelForm (see imported forms above)

class LogNewFeatureForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("client_code", "user_id", "assigned_client_user", "assigned_vendor_user", "software_component", "title", "summary", "details", "paid", "status", "price")

class FeatureStatusForm(forms.ModelForm):
   
    class Meta:
        model = Feature
        fields = ("status",)



