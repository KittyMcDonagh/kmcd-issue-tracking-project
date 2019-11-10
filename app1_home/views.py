from django.shortcuts import render
from django.contrib import messages
from accounts.forms import UserLoginForm
from app2_user_home.models import UserDetail
from app2_user_home.models import Vendor
from app2_user_home.models import Customer


# Home Page
def home(request):
    
    """ A view that renders the home page """
    
    # Check whether user is logged in
    
    if request.user.is_authenticated: 
        login_form = UserLoginForm(request.POST)
    
        # User already logged in. Get the user details from the Issue Tracking System
    
        UserDetails = UserDetail.objects.get(user_name=request.user.username)
        messages.success(request, "You are already logged in!")
    
        # Get the Vendor or Customer Details depending on which the user is 
        # associated with
        
        CustomerDetails = ""
        VendorDetails = ""
    
        if UserDetails.user_type == 'C':
        
            try:
                CustomerDetails = Customer.objects.get(cust_code=UserDetails.vend_cust_code)
            except:
                messages.success(request, "Customer details not found!")
    
        else:
            try:
                VendorDetails = Vendor.objects.get(vend_code=UserDetails.vend_cust_code)
            except:
                messages.success(request, "Vendor details not found!")
    
        return render(request, 'home.html', {'userdetails': UserDetails, 'customerdetails': CustomerDetails, 'vendordetails': VendorDetails })
    
    else:
        return render(request, "home.html")
    
