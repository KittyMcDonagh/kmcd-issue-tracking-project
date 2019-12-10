# Initial code copied from the e-commerce project

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import JsonResponse 


"""
A view that renders the cart contents page
"""

def view_cart(request):

    # We dont need to return a dictionary because the cart context is available
    # to all pages
    
    return render(request, 'cart.html')
    

"""
Add a quantity of the specified feature id to the cart
""" 

def add_to_cart(request, id):
    
    print("in add_to_cart, id -------------------------------------")
        
    # This takes an integer from the form we created
    
    print("request method: "+str(request.method))
    print("id: "+str(id))
    
    # Get the quantity we specified
    
    quantity = int(request.POST.get('quantity'))
    
    print("quantity: "+str(quantity))
    
    # This is going to the cart from the session (not from the database), 
    # and it gets a cart if one already exists, otherwise it gets an empty
    # dictionary
    
    print("about to get cart----------------------------------------")
    cart = request.session.get('cart', {})
    print("have cart----------------------------------------")
        
    # Add cart id and quantity
    
    if id in cart:
        cart[id] = int(cart[id]) + quantity
        
    else:
        cart[id] = cart.get(id, quantity)
        
    request.session['cart'] = cart
        
    return redirect(reverse('features_home'))
        

# This view is called via the js (".add-btn-click") in base.html

def add_to_cart_js(request):
    
    print("in add_to_cart_js -------------------------------------")
        
    # This takes an integer from the form we created
    
    print("request method: "+str(request.method))
    
    id = int(request.POST.get('featureId'))
    quantity = int(request.POST.get('qty'))
    
    print("id: "+str(id))
    print("quantity: "+str(quantity))
    
    # This is going to get the cart from the session (not from the database), 
    # and it gets a cart if one already exists, otherwise it gets an empty
    # dictionary
    
    print("about to get cart_js----------------------------------------")
    cart = request.session.get('cart', {})
    print("have cart_js----------------------------------------")
        
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
Adjust the quantity of the specified feature to the specified amount
"""
def adjust_cart(request, id):
    
    # This takes an integer from the form we created
    
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
    
    return redirect(reverse('view_cart'))
    
    
