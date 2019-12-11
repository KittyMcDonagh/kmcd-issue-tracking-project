# NOTE: This was copied from the ecommerce project

from django.shortcuts import render

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Note: strip is installed using "sudo pip3 install stripe"

import stripe
from .forms import OrderForm, MakePaymentForm
from django.conf import settings
from django.utils import timezone
from app4_features.models import Feature
from app4_features.forms import FeatureAmountPaidForm
from .models import OrderLineItem

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    
    print("in checkout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if request.method=="POST":
        print("in checkout- POST====================================================")
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            print("forms are valid-------------------------------------------")
            order = order_form.save()
            print("form saved: order.date = "+str(order.date))
            
            order.date = timezone.now()
            print("date saved: order.date = "+str(order.date))
            
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
                
            # Multiplying by 100 below to add decimals (Dont put comments into the middle of ())
            # We will see user email in the stripe dashboard. It will
            # tell us who the payment came from
            # Stripe does all the security, but we have to inform our customer
            # if there's a problem
            
            print("ABOUT TO TRY PAYING---------------------------------------")
            try:
                customer = stripe.Charge.create(
                    amount= int(total * 100),
                    currency = 'EUR',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id']
                    )
            
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            print("CHECKING CUSTOMER.PAID---------------------------------------")
            
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                
                request.session['cart'] = {}
                return redirect(reverse('features_home'))
                
            else:
                 messages.error(request, "Unable to take payment")
        
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card!")
            
    else:
        print("in checkout- !POST====================================================")
        payment_form = MakePaymentForm()
        order_form = OrderForm
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
    
    
    
    
    
