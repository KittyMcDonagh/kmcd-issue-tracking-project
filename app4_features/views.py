from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from django.http import JsonResponse 

from datetime import datetime

from app2_user_home.models import Vendor
from app2_user_home.models import Client
from app2_user_home.models import UserDetail
from .models import Feature


"""
Features list page
"""

def my_features_list(request):
    
    # Initialise the Feature filters
    
    SelectedFeaturesFilter = "ASSIGNED TO ME"
    
    # Set Client Filter to ALL
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter to ALL
    
    SelectedStatusFilter = "ALL"
    
    # set Priority Filter to ALL
    
    SelectedPaidFilter = "ALL"
    
    # Initialise these details in case user is not set up on Issue Tracker
    
    AllClients = ""
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracking system. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        # Get all clients for Client Dropdown - only available to Vendor-side 
        # users
            
        AllClients = get_all_clients(request)
            
            
    # Get all Features
    
    Features = ""
    
    # Get the Issues assigned to the logged only. 
    # An issue can be assigned both to a client-side user and a vendor-side user, 
    # so we need to verify which one it is
    
    if UserDetails.user_type == "C":
            
        # User is on the Client side
    
        print("client-user: "+str(UserDetails.user_id))
        
        try:
            Features = Feature.objects.filter(assigned_client_user=UserDetails.user_id)
        except:
            messages.error(request, "PROBLEM RETRIEVING FEATURES!")
    
    else:
        # User is on the Vendor side
        
        try:
            Features = Feature.objects.filter(assigned_vendor_user=UserDetails.user_id)
        except:
            messages.error(request, "PROBLEM RETRIEVING FEATURES!")
                
        
    
    print("FEATURES: "+str(Features))
    
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Features = FinalFilterIssues(request, Features, UserDetails)
                
    
    # For Pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(Features, 5)
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    
    # Pass features back as 'listing'. It will be used to pick up the pagination
    # variables in base.html. The same will be done with the issues list.
    
    listing = features
  
    return render(request, 'featureslist.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'features': features, "listing":listing })


"""
Get all the features and display as a table list
"""

def all_features_list(request):
    
    # Initialise all the filters to 'ALL'
    
    SelectedFeaturesFilter = "ALL"
    
    # Set Client Filter to ALL
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter to ALL
    
    SelectedStatusFilter = "ALL"
    
    # Initialise these details in case user is not set up on Issue Tracker
    
    AllClients = ""
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracking system. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The Issues Filte
        # values the client user can use, and the filtered Issues
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
            
        # Get all clients for Client Dropdown - only available to Vendor-side 
        # users
            
        AllClients = get_all_clients(request)
        

    # Get all issues
    
    Features = Feature.objects.all()
    
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Features = FinalFilterIssues(request, Features, UserDetails)

    # For Pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(Features, 5)
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    
     # Pass features back as 'listing'. It will be used to pick up the pagination
    # variables in base.html. The same will be done with the issues list.
    
    listing = features
  
    return render(request, 'featureslist.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'features': features, 'all_clients': AllClients, 'selected_features_filter':SelectedFeaturesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter, "listing":listing })


"""
Create a view that returns a single Post object based on the Post ID(pk)
and render it to the 'postdetail.html' template or return a 404 error if
the Post is not found.
"""
def feature_details(request, pk):
    
    # Retrieve the issue
    
    feature = get_object_or_404(Feature, pk=pk)
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
    ClientDetails = ""
    VendorDetails = ""
    IssueClientDetails = ""
    
    # Get the user's details from re the issue tracking system. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
    
    FeatureClientDetails = ""
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The Issues Filte
        # values the client user can use, and the filtered Issues
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        FeatureClientDetails = get_feature_client_details(request, feature)
    
    return  render(request, 'featuredetails.html', {'feature': feature, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "featureclientdetails": FeatureClientDetails})
    



"""
Get the logged in user's details re the Issue Tracking System. 
These details tells us whether the User is on the Vendor side or 
the Client side.
"""
    
def get_user_iss_trk_details(request):
    
    UserDetails = ""

    try:
        UserDetails = UserDetail.objects.get(user_id=request.user.username)
    except:
        messages.error(request, "Problem retrieving the user's Issue Tracker Details!")
    
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
    

"""
All Client records needed for Client Dropdown if Vendor user is logged in 
"""

def get_all_clients(request):
    
    AllClients = ""

    try:
        AllClients = Client.objects.all()
    except:
        messages.error(request, "Problem retrieving all Client Records!")
   
    return  AllClients
    
    
"""
The logged in user is on the Vendor side - get the Vendor details
"""
def get_vendor(request, UserDetails):
        
        try:
            VendorDetails = Vendor.objects.get(vend_code=UserDetails.vend_client_code)
        except:
            messages.error(request, "Vendor details not found!")
        
        return  VendorDetails
        
        
"""
Get the details of the Client the Feature belongs to. This is required for a Vendor
user only. Although Client-side users see other clients' features, they dont see
the details of those clients.
"""
def get_feature_client_details(request, feature):
    
    FeatureClientDetails = ""

    try:
        FeatureClientDetails = Client.objects.get(client_code=feature.client_code)
    except:
        messages.error(request, "Feature Client details not found!")
        
    return FeatureClientDetails


"""
Final filter to make sure users see only what they're allowed to see.
Vendors can only see features when they reach status of 'LOGGED' (i.e. they cannot
see 'DRAFT')
Clients cannot see features of other clients that are of status 'DRAFT' or 'LOGGED'
"""

def FinalFilterIssues(request, Features, UserDetails):
    
    if UserDetails.user_type == "V":
        
        # This is a Vendor-side user
        # Vendors cannot see features until they reach status 'LOGGED'
                
        Features = Features.exclude(status = "DRAFT")
    
    else:
        
        # Client-side users cannot see features of other clients that are still
        # at status 'DRAFT' or 'LOGGED'
        
        # Separating our clients from other clients, so that I can filter other 
        # clients issues by status
        
        OurClientsFeatures = Features.filter(client_code = UserDetails.vend_client_code)
        
        OtherClientsFeatures = Features.exclude(client_code = UserDetails.vend_client_code)
        OtherClientsFeatures = OtherClientsFeatures.exclude(status = "DRAFT").exclude(status = "LOGGED")
        
        # Putting the two lists together after filtering other clients issues
        
        Features = OurClientsFeatures | OtherClientsFeatures
    
    # Sorting issues by date, descending order
        
    Features = Features.order_by('-input_date')
        
    return Features
