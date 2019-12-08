from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from django.http import JsonResponse 

from datetime import datetime

from app2_user_home.models import Vendor
from app2_user_home.models import Client
from app2_user_home.models import UserDetail


from app3_issue_logging.models import Issue

# Search view

def search_issues(request):
    print("==================================================================")
    print("REQUEST: "+str(request))
    print("==================================================================")
    
     # Initialise the issue filters
    
    SelectedIssuesFilter = "ASSIGNED TO ME"
    
    # Set Client Filter to ALL
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter to ALL
    
    SelectedStatusFilter = "ALL"
    
    # set Priority Filter to ALL
    
    SelectedPriorityFilter = "ALL"
    
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
            
        # User is on the Client side. Get the Client Details, The issues Filter
        # values the client user can use, and the filtered issues
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
            
        # Get all clients for Client Dropdown - only available to Vendor-side 
        # users
            
        AllClients = get_all_clients(request)

    # Get whatever is returned on the form. Form name = 'q'. Whatever is typed
    # into this form will be used to filter the products
    
    Issues = Issue.objects.filter(software_component__icontains=request.GET['q_issues'])
    
    search_value = request.GET['q_issues']
   
    print("search_value: "+str(search_value))
    
    # For Pagination
    print("request.method: "+str(request.method))
    
    page = request.GET.get('page', 1)
    paginator = Paginator(Issues, 5)
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
    
    # Pass issues back as 'listing'. It will be used t pick up the pagination
    # variables in base.html. The same will be done with the features list.
    
    listing = issues
    list_type = "issues"
    searching = 'y'
    
    print("searching: "+str(searching))
  
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': issues, 'all_clients': AllClients, 'selected_issues_filter':SelectedIssuesFilter, 'selected_status_filter': SelectedStatusFilter, 'selected_priority_filter': SelectedPriorityFilter, 'selected_client_filter': SelectedClientFilter, "listing":listing, "list_type": list_type, "search_value": search_value, "searching": searching})


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