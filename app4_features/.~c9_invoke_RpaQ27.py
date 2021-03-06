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
Features home page
"""

def features_home(request):
    
    print("in features_home")
    
    # Initialise the feature filters
    
    SelectedFeaturesFilter = "ASSIGNED TO ME"
    
    # Set Client Filter to ALL
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter to ALL
    
    SelectedStatusFilter = "ALL"
    
    # set Paid Filter to ALL
    
    SelectedPaidFilter = "ALL"
    
    # Initialise these details in case user is not set up on the Issue Tracker app
    
    AllClients = ""
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the Issue Tracker app. It has already
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
            
            
    # Get all features
    
    Features = ""
    
    # Get the features assigned to the logged in user only. 
    # A feature can be assigned both to a client-side user and a vendor-side user, 
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
    
    Features = FinalFilterFeatures(request, Features, UserDetails)
                
    
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
  
    return render(request, 'featuresh.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'features': features, 'selected_features_filter':SelectedFeaturesFilter, 'selected_status_filter': SelectedStatusFilter, "selected_paid_filter": SelectedPaidFilter, 'selected_client_filter': SelectedClientFilter, "listing":listing })


"""
Get all the features and display as a table list
"""

def all_features_list(request):
    
    print("in all_features_list")
    
    # Initialise all the filters to 'ALL'
    
    SelectedFeaturesFilter = "ALL"
    
    # Set Client Filter to ALL
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter to ALL
    
    SelectedStatusFilter = "ALL"
    
    # set Paid Filter to ALL
    
    SelectedPaidFilter = "ALL"
    
    # Initialise these details in case user is not set up on Issue Tracker app
    
    AllClients = ""
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the Issue Tracker app. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The features Filter
        # values the client user can use, and the filtered features
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
            
        # Get all clients for Client Dropdown - only available to Vendor-side 
        # users
            
        AllClients = get_all_clients(request)
        

    # Get all features
    
    Features = Feature.objects.all()
    
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Features = FinalFilterFeatures(request, Features, UserDetails)

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
  
    return render(request, 'featureslist.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'features': features, 'all_clients': AllClients, 'selected_features_filter':SelectedFeaturesFilter, 'selected_status_filter': SelectedStatusFilter, "selected_paid_filter": SelectedPaidFilter, 'selected_client_filter': SelectedClientFilter, "listing":listing })


"""
This function is called via the javascript in base.html
Get the features, filtered by the features Filter options selected
"""
def get_features(request):
    
    print("in get_features ------------------------------------------>")
    
    data = []
    
    # Get the user's details relating to the Issue Tracker app - it has
    # already been established that the user's details exist, otherwise they
    # wouldnt have got this far
            
    UserDetails = get_user_iss_trk_details(request)
        
    # Get all the features from the features database
        
    Features = Feature.objects.all()
    
    print("after 'Feature.objects.all()' ")
    
    # Get the filters - passed from the js in base.html
        
    features_filter = request.POST.get('featuresFilter')
    status_filter = request.POST.get('statusFilter')
    paid_filter = request.POST.get('paidFilter')
    client_filter = request.POST.get('clientFilter')
    
    print("features_filter: "+str(features_filter))
    print("status_filter: "+str(status_filter))
    print("paid_filter: "+str(paid_filter))
    print("client_filter: "+str(client_filter))
    
    print("STILL in get_features ------------------------------------------>")
    
    
    # User has requested all features assigned to them?
            
    if features_filter == 'ASSIGNED TO ME':
                
        # Is this a Client-side user?
                
        if UserDetails.user_type == "C":
    
            Features = Features.filter(assigned_client_user = UserDetails.user_id)
    			
        else:
                
            # This is a Vendor-side user
                
            Features = Features.filter(assigned_vendor_user = UserDetails.user_id)
                
    else:
                
        # Has user requested 'Our Features Only'?
        # This option is relevant to Client-side users only'
                
        if features_filter == 'OUR FEATURES ONLY':
                    
            Features = Features.filter(client_code = UserDetails.vend_client_code)
                            
        else:
                    
            # Has user requested 'Other Clients' features Only?
                
            if features_filter == "OTHER CLIENTS' FEATURES ONLY":
            
                Features = Features.exclude(client_code = UserDetails.vend_client_code)
        
    # Filter features further if status filter is set . . .
        
    if status_filter != "ALL":
        Features = Features.filter(status=status_filter)
        
    # . . . or if Client filter is set (client filter is availabe to vendor
    # -side users only)
        
    if client_filter != "ALL":
        Features = Features.filter(client_code=client_filter)
        
    # . . . or if Paid filter is set 
    
    print("Before filtering by paid: paid_filter "+str(paid_filter))
        
    if paid_filter != "ALL":
        Features = Features.filter(paid=paid_filter)
        
    print("After filtering by paid: paid_filter "+str(paid_filter))
        
    
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Features = FinalFilterFeatures(request, Features, UserDetails)
    
    user_message = ""
    
    if not Features:
        user_message = "No features found for the selected criteria!"
    
    print("user_message: "+str(user_message))

    # For Pagination
    
    print("request.method: "+str(request.method))
    
    page = request.POST.get('page', 1)
    
    print("page = "+str(page))
    
    paginator = Paginator(Features, 5)
    
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
        
    # Save the pagination parameters for use in the js function in base.html
    # that called 'get_features'
        
    has_other_pages = features.has_other_pages()
    has_prev_page = features.has_previous()
    current_page = features.number
    has_next_page = features.has_next()
    
    prev_page_nr = 0
    if features.has_previous():
        prev_page_nr = features.previous_page_number()
        
    next_page_nr = 0
    if features.has_next():
        next_page_nr = features.next_page_number()
        
    page_range = paginator.page_range
    
    # Create data dictionary to return to the js function (in base.html)
    
    data = {}

    # Return the pagination parameters to js for output to the html file
    
    data["pagination_props"] = {
		"has_other_pages": has_other_pages,
		"has_prev_page": has_prev_page,
		"current_page": current_page,
		"has_next_page": has_next_page,
		"prev_page_nr": prev_page_nr,
		"next_page_nr": next_page_nr,
		"page_range": list(page_range)
	}
	
    # Return the user message also - set above if no features found
    
    data["user_mesg"] = {
        
        "user_message": user_message
	  }
	
	# Return the features to be output to  the html table
	
    data["features"] = []
   
    for feature in features:
        data["features"].append({
            
            "id": feature.id,
        	"title": feature.title,
        	"details": feature.details,
        	"client_code": feature.client_code,
            "date": datetime.strftime(feature.input_date, '%d %b %y'),
        	"user": feature.user_id,
        	"assigned_client_user": feature.assigned_client_user,
        	"assigned_vendor_user": feature.assigned_vendor_user,
        	"software_component": feature.software_component,
        	"paid": feature.paid,
        	"summary": feature.summary,
        	"status": feature.status,
        	"user_type": UserDetails.user_type
    })
    
    print("returning to js")
        
    return JsonResponse(data, safe=False)




"""
Create a view that returns a single Post object based on the Post ID(pk)
and render it to the 'postdetail.html' template or return a 404 error if
the Post is not found.
"""
def feature_details(request, pk):
    
    # Retrieve the feature
    
    feature = get_object_or_404(Feature, pk=pk)
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
    ClientDetails = ""
    VendorDetails = ""
    FeatureClientDetails = ""
    
    # Get the user's details from re the Issue Tracker app. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
    
    FeatureClientDetails = ""
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The features Filter
        # values the client user can use, and the filtered Features
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        FeatureClientDetails = get_feature_client_details(request, feature)
    
    return  render(request, 'featuredetails.html', {'feature': feature, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "featureclientdetails": FeatureClientDetails})
    



"""
Get the logged in user's details re the Issue Tracker app. 
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
Get the details of the Client the feature belongs to. This is required for a Vendor
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

def FinalFilterFeatures(request, Features, UserDetails):
    
    if UserDetails.user_type == "V":
        
        # This is a Vendor-side user
        # Vendors cannot see features until they reach status 'LOGGED'
                
        Features = Features.exclude(status = "DRAFT")
    
    else:
        
        # Client-side users cannot see features of other clients that are still
        # at status 'DRAFT' or 'LOGGED'
        
        # Separating our clients from other clients, so that I can filter other 
        # clients features by status
        
        OurClientsFeatures = Features.filter(client_code = UserDetails.vend_client_code)
        
        OtherClientsFeatures = Features.exclude(client_code = UserDetails.vend_client_code)
        OtherClientsFeatures = OtherClientsFeatures.exclude(status = "DRAFT").exclude(status = "LOGGED")
        
        # Putting the two lists together after filtering other clients features
        
        Features = OurClientsFeatures | OtherClientsFeatures
    
    # Sorting features by date, descending order
        
    Features = Features.order_by('-input_date')
        
    return Features
