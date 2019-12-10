# NOTE: This was copied from the ecommerce project

from django import forms

from .models import Order

class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2040)]
    
    # Stripe will do the encrytion of the details, via its javascript. That's 
    # why we can do required=False here, so that the plain text is not 
    # transmitted through the browser. Therefore, it makes it more secure.
    # It's not visible to people who might be snooping on the webpage.
    
    credit_card_number = forms.CharField(label="Credit card number", required=False)
    cvv = forms.CharField(label="Security code (CVV)", required=False) 
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    
    # The following field will not be seen by the user (HiddenInput), but data
    # will be input into it, as stripe requires this field.
    
    stripe_id = forms.CharField(widget=forms.HiddenInput)

# Online order form

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
        
        
        
