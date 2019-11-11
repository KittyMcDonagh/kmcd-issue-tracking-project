from django.shortcuts import render
from django.contrib import messages
from accounts.forms import UserLoginForm
from app2_user_home.models import UserDetail
from app2_user_home.models import Vendor
from app2_user_home.models import Client


# Home Page
def home(request):
    
    """ A view that renders the home page """
    
    # Check whether user is logged in
    
    if request.user.is_authenticated: 
        login_form = UserLoginForm(request.POST)
    
        # User already logged in. Get the user details from the Issue Tracking System
    
        UserDetails = UserDetail.objects.get(user_name=request.user.username)
        messages.success(request, "You are already logged in!")
    
        # Get the Vendor or Client Details depending on which the user is 
        # associated with
        
        ClientDetails = ""
        VendorDetails = ""
    
        if UserDetails.user_type == 'C':
        
            try:
                ClientDetails = Client.objects.get(client_code=UserDetails.vend_client_code)
            except:
                messages.success(request, "Client details not found!")
    
        else:
            try:
                VendorDetails = Vendor.objects.get(vend_code=UserDetails.vend_client_code)
            except:
                messages.success(request, "Vendor details not found!")
    
        return render(request, 'home.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails })
    
    else:
        return render(request, "home.html")
    
