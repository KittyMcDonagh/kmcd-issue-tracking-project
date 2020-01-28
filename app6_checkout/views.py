# NOTE: This code was copied from the ecommerce project and adjusted

from django.shortcuts import render

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Note: strip is installed using "sudo pip3 install stripe"

import stripe
from .forms import OrderForm, MakePaymentForm
from django.conf import settings
from django.utils import timezone
from app2_user_home.models import UserDetail
from app4_features.models import Feature, FeaturePaid
from app4_features.forms import FeatureAmountPaidForm
from .models import OrderLineItem

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    
    # Get the user's details from the user details db. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    if request.method=="POST":
        
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save()
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            
            for id, quantity, in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += quantity * feature.price
                order_line_item = OrderLineItem(
                    order = order,
                    feature = feature,
                    quantity = quantity
                    )
                order_line_item.save()
                
            # Multiplying by 100 below to add decimals.
            # User email will appear in the stripe dashboard. It will
            # indicate who the payment came from.
            # Stripe does all the security and returns an error status.
            # If stripe returns an error, a message will be sent to the 
            # an user
            
            try:
                customer = stripe.Charge.create(
                    amount= int(total * 100),
                    currency = 'EUR',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id']
                    )
            
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                
                for id, quantity, in cart.items():
                    feature = get_object_or_404(Feature, pk=id)
                    
                    # Total amount paid for Feature = quantity * Feature price
                
                    ftr_amount_paid = quantity * feature.price
                    
                    # If this a record doesnt exist for this Feature, for this client, create it
                    # (I got help with this code from @mormoran on Slack :-) )
        
                    feature_paid, created = FeaturePaid.objects.get_or_create(feature_id=id, client_code = UserDetails.vend_client_code, defaults={ "user_id":UserDetails.user_id, "author": feature.client_code, "quantity":quantity, "amount_paid":ftr_amount_paid})
                    
                    # If Feature Paid record already exists for this client (i.e. did not have to be created above), update it
                    
                    if not created:
                        
                        # A Feature paid record exists for this Feature for this client
                        # Update the amount paid and quantity
                        
                        feature_paid.amount_paid = feature_paid.amount_paid + ftr_amount_paid
                        
                        feature_paid.quantity = feature_paid.quantity + quantity
                        
                        feature_paid.save()
                        
                
                    # Update the Feature total amount paid so far
                    
                    feature.paid += ftr_amount_paid
                    
                    # If a new Feature paid record was created for a client,
                    # increment the client count. This is the number of
                    # individual clients who have flagged this Feature
                    
                    if created:
                        feature.client_count += 1
                        
                    feature.save()
                    
                # Clear the cart
                
                request.session['cart'] = {}
                
                messages.error(request, "You have successfully paid")
                return redirect(reverse('features_home'))
                
            else:
                 messages.error(request, "Unable to take payment")
        
        else:
            messages.error(request, "We were unable to take payment with that card!")
            
    else:
        # Return empty payment form
        
        payment_form = MakePaymentForm()
        order_form = OrderForm
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
    

"""
Get the logged in user's details the user details db. 
These details tells us whether the User is on the Vendor side or 
the Client side.
"""
    
def get_user_iss_trk_details(request):
    
    UserDetails = ""

    try:
        UserDetails = UserDetail.objects.get(user_id=request.user.username)
    except:
        messages.error(request, "Problem retrieving the user's details!")
    
    return UserDetails
    
    
    
    
