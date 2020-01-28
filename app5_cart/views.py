# Initial code copied from the e-commerce project

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse 

from app2_user_home.models import Vendor
from app2_user_home.models import Client
from app2_user_home.models import UserDetail


# NOTE: The code for the cart and checkout was copied from the ecommerce project
# we did on the course and adjusted.

"""
A view that renders the cart contents page
"""

def view_cart(request):
    
    # Get the user's details from the user details db. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Only a client-side user would be in the cart.
    # Get the Client Details
            
    ClientDetails = get_client(request, UserDetails)

    # We dont need to return a dictionary because the cart context is available
    # to all pages
    
    return render(request, 'cart.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails })
    

"""
When the user clicks on the thumbs up button -
Add 1 to the specified Feature id count in the cart
""" 

def add_to_cart(request, id):
    
    # This takes an integer from the form we created
    
    # Get the quantity we specified
    
    quantity = 1
   
    # This is going to the cart from the session (not from the database), 
    # and it gets a cart if one already exists, otherwise it gets an empty
    # dictionary
    
    cart = request.session.get('cart', {})
    
    # Add cart id and quantity
    
    if id in cart:
        
        cart[id] = int(cart[id]) + quantity
        
    else:
        
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
        
    return redirect(reverse('features_home'))
        

# This view is called via the js (".add-btn-click") in base.html

def add_to_cart_js(request):
        
    # This takes an integer from the form we created
    
    id = request.POST.get('featureId')
    quantity = int(request.POST.get('qty'))
    
    # This is going to get the cart from the session (not from the database), 
    # and it gets a cart if one already exists, otherwise it gets an empty
    # dictionary
    
    cart = request.session.get('cart', {})
   
    # Add cart id and quantity
    
    if id in cart:
        
        cart[id] = int(cart[id]) + quantity
        
    else:

        cart[id] = cart.get(id, quantity)
    
    # Update the cart
    
    request.session['cart'] = cart
    
    data = {}
    
    data["cart"] = {
        
        "qty":quantity
        
        }
    
    return JsonResponse(data, safe=False)



"""
Adjust the quantity of the specified Feature to the specified amount
"""
def adjust_cart(request, id):
    
    # This takes teh quantity from the form
    
    quantity = int(request.POST.get('quantity'))
    
    # This is going to the cart from the session (not from the database), 
    # and it gets a cart if one already exists, otherwise it gets an empty
    # dictionary
        
    cart = request.session.get('cart', {})
    
    # Only adjust the cart if 'quantity' is greater than zero
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    
    # If the cart is empty, return to the Features list, otherwise go back
    # to the cart list
    
    
    if not cart:
        return redirect(reverse('features_home'))
    else:
        return redirect(reverse('view_cart'))
    
   
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
    

"""
The logged in user is on the Client side - get the Client details
"""

def get_client(request, UserDetails):

    try:
        ClientDetails = Client.objects.get(client_code=UserDetails.vend_client_code)
    except:
        messages.error(request, "Client details not found!")
   
    return  ClientDetails
    
 
