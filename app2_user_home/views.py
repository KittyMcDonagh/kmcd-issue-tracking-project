from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

from .models import Vendor
from .models import Client
from .models import UserDetail
from app3_issue_logging.models import Issue

from accounts.forms import UserLoginForm



"""
User Home Page - Initial load or when user selects "ISSUES ASSIGNED TO ME"
Issues assigned to the logged in user are shown.
"""

def userhome(request):
    
    # Set the filters' default values
    
    SelectedIssuesFilter = "ASSIGNED TO ME"
    
    # Set Client Filter 
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter
    
    SelectedStatusFilter = "ALL"
    
    
    # Confirm that the logged in user is set up on the Issue Tracking System 
    # These details tells us whether the User is on the Vendor side or 
    # the Client side.
    
    UserDetails = issue_tracker_user_details(request)
    
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
    
    AllClients = ""
    ClientDetails = ""
    VendorDetails = ""
    
    if UserDetails.user_type == 'C':
        
        # User is on the Client side. Get the Client Details, The Issues Filte
        # values the client user can use, and the filtered Issues
        
        ClientDetails = get_client(request, UserDetails)
    
    else:
        
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        # Get all clients for Client Dropdown
        
        AllClients = get_all_clients(request)
        
    
    # Get the Issues based on selected filter
    
    Issues = get_issues(request, UserDetails, SelectedIssuesFilter)
        
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': Issues, 'all_clients': AllClients, 'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter })
    

"""
User has requested to see ALL ISSUES
"""

def all_issues(request):
    
    # Set the filter value
    
    SelectedIssuesFilter = "ALL ISSUES"
    
    # Set Client Filter 
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter
    
    SelectedStatusFilter = "ALL"
    
    
    # Get the logged in user's details re the Issue Tracking System
    
    UserDetails = issue_tracker_user_details(request)
   
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
    
    AllClients= ""
    ClientDetails = ""
    VendorDetails = ""
    
    
    if UserDetails.user_type == 'C':
        
        # User is on the Client side. Get the Client Details, The Issues Filte
        # values the client user can use, and the filtered Issues
        
        ClientDetails = get_client(request, UserDetails)
    
    else:
        
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        # Get all clients for Client Dropdown
        
        AllClients = get_all_clients(request)
        
        
    # Get the Issues based on selected filter
    
    Issues = get_issues(request, UserDetails, SelectedIssuesFilter)
        
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': Issues, 'all_clients': AllClients,'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter })


"""
User has requested to see OUR ISSUES ONLY
"""

def our_issues_only(request):
    
    # Set the filter value
    
    SelectedIssuesFilter = "OUR ISSUES ONLY"
    
    # Set Client Filter 
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter
    
    SelectedStatusFilter = "ALL"
    
    
    # Get the logged in user's details re the Issue Tracking System
    
    UserDetails = issue_tracker_user_details(request)
   
    
    # "OUR ISSUES ONLY" option is relevant to the Client side user only 
    
    ClientDetails = ""
    VendorDetails = ""
        
    # User is on the Client side. Get the Client Details, The Issues Filte
    # values the client user can use, and the filtered Issues
        
    ClientDetails = get_client(request, UserDetails)
    
    
    # Get the Issues for the Client associated with the logged in user only
    
    Issues = get_issues(request, UserDetails, SelectedIssuesFilter)
        
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': Issues, 'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter })


"""
User has requested to see OTHER CLIENTS' ISSUES ONLY
"""

def other_clients_issues_only(request):
    
    # Set the filter value
    
    SelectedIssuesFilter = "OTHER CLIENTS' ISSUES ONLY"
    
    # Set Client Filter 
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter
    
    SelectedStatusFilter = "ALL"
    
    
    # Get the logged in user's details re the Issue Tracking System
    
    UserDetails = issue_tracker_user_details(request)
   
    
    # "OTHER CLIENTS' ISSUES ONLY" option is relevant to client user only
    
    ClientDetails = ""
    VendorDetails = ""
    
    
    
        
    # User is on the Client side. Get the Client Details, The Issues Filte
    # values the client user can use, and the filtered Issues
        
    ClientDetails = get_client(request, UserDetails)
    
    # Get the Issues for clients other than the client associated with the logged
    # in user
    
    Issues = get_issues(request, UserDetails, SelectedIssuesFilter)
        
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': Issues, 'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter })



"""
Get the logged in user's details re the Issue Tracking System. 
These details tells us whether the User is on the Vendor side or 
the Client side.
"""
    
def issue_tracker_user_details(request):

    try:
        UserDetails = UserDetail.objects.get(user_name=request.user.username)
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
Get the Issues, filtered by the Issues Filter option selected
"""

def get_issues(request, UserDetails, SelectedIssuesFilter):
    
    Issues = ""
    
    # If the selection is to get all issues assigned to the logged in user,
    # show the issues assigned to the client user or the vendor user, depending
    # on the user type
    
    if SelectedIssuesFilter == "ASSIGNED TO ME":
        
        if UserDetails.user_type == "C":
            
            # User is on the Client side
            
            try:
                Issues = Issue.objects.filter(assigned_client_user=UserDetails.user_name)
                messages.success(request, "Client Issues successfully retrieved!")
            except:
                messages.error(request, "PROBLEM RETRIEVING CLIENT ISSUES!")
        
        else:
            
            # User is on the Vendor side
        
            try:
                Issues = Issue.objects.filter(assigned_vendor_user=UserDetails.user_name)
                messages.success(request, "Vendor Issues successfully retrieved!")
            except:
                messages.error(request, "PROBLEM RETRIEVING VENDOR ISSUES!")
    
    else:
        
        if SelectedIssuesFilter == "ALL ISSUES":
            
            try:
                Issues = Issue.objects.all()
                messages.success(request, "All Issues successfully retrieved!")
            except:
                messages.error(request, "PROBLEM RETRIEVING ALL ISSUES!")
    
        else:
            
            if SelectedIssuesFilter == "OUR ISSUES ONLY":
                
                # "OUR ISSUES ONLY" is relevant to Client side users only
                
                try:
                    Issues = Issue.objects.filter(client_code=UserDetails.vend_client_code)
                    messages.success(request, "Our Client Issues successfully retrieved!")
                except:
                    messages.error(request, "PROBLEM RETRIEVING OUR CLIENT ISSUES!")
            
            else:
            
                if SelectedIssuesFilter == "OTHER CLIENTS' ISSUES ONLY":
                
                    # "OTHER CUSTOMERS' ISSUES ONLY" is relevant to Client side users only
                    
                    try:
                        Issues = Issue.objects.exclude(client_code=UserDetails.vend_client_code)
                        messages.success(request, "Our Client Issues successfully retrieved!")
                    except:
                        messages.error(request, "PROBLEM RETRIEVING OUR CLIENT ISSUES!")
    
    return  Issues
    
    
    """
    Trying jQuery option
    """
    
    """
User has requested to see ALL ISSUES
"""

def jq_issues(request):
    
    # Set the filter value
    
    SelectedIssuesFilter = "ALL ISSUES"
    
    # Set Client Filter 
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter
    
    SelectedStatusFilter = "ALL"
    
    
    # Get the logged in user's details re the Issue Tracking System
    
    UserDetails = issue_tracker_user_details(request)
   
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
    
    AllClients= ""
    ClientDetails = ""
    VendorDetails = ""
    
    
    if UserDetails.user_type == 'C':
        
        # User is on the Client side. Get the Client Details, The Issues Filte
        # values the client user can use, and the filtered Issues
        
        ClientDetails = get_client(request, UserDetails)
    
    else:
        
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        # Get all clients for Client Dropdown
        
        AllClients = get_all_clients(request)
        
        
    # Get the Issues based on selected filter
    
    Issues = get_issues(request, UserDetails, SelectedIssuesFilter)
        
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': Issues, 'all_clients': AllClients,'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter })

