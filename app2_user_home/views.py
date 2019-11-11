from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Vendor
from .models import Client
from .models import UserDetail

from accounts.forms import UserLoginForm

# User Home Page
def userhome(request):
    
    """
    The accounts login has already verified that this user is set up on the 
    Issue Tracking System. Retrieve the details here again before going to the
    User's home page
    """
    
    UserDetails = UserDetail.objects.get(user_name=request.user.username)
    
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
        
    
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails })
    

