from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Vendor
from .models import Client
from .models import UserDetail
from app3_issue_logging.models import FilterForClient
from app3_issue_logging.models import FilterForVendor
from app3_issue_logging.models import StatusFilter

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
        
        try:   
            Filter = FilterForClient.objects.all()
        except:
            messages.success(request, "Problem Client filter!")
    
    else:
        try:
            VendorDetails = Vendor.objects.get(vend_code=UserDetails.vend_client_code)
        except:
            messages.success(request, "Vendor details not found!")
        
        try:
            Filter = FilterForVendor.objects.all()
        except:
            messages.success(request, "Problem with Vendor filter!")
    
    try:
        Status = StatusFilter.objects.all()
    except:
        messages.success(request, "Problem with Status filter!")
            
        
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'filter': Filter, 'status': Status })
    
    

