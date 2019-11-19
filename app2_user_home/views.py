from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import HttpResponse
from django.http import JsonResponse 

from datetime import datetime

from .models import Vendor
from .models import Client
from .models import UserDetail
from app3_issue_logging.models import Issue

from accounts.forms import UserLoginForm


"""
User Home Page - Initial load
Issues assigned to the logged in user are shown.
"""

def userhome(request):
    
    # Set the filters' default values
    
    SelectedIssuesFilter = "ASSIGNED TO ME"
    
    # Set Client Filter 
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter
    
    SelectedStatusFilter = "ALL"
    
    # Initialise these details in case user is not set up on Issue Tracker
    
    AllClients = ""
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracking system. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = issue_tracker_user_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The Issues Filte
        # values the client user can use, and the filtered Issues
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
            
        # Get all clients for Client Dropdown
            
        AllClients = get_all_clients(request)

    Issues = ""
    
    # We are showing the Issues assigned to the logged in user, for all Statuses
    # and all Clients.
    # An issue can be assigned both to a client-side user and a vendor-side user, 
    # so we need to verify which one it is
        
    if UserDetails.user_type == "C":
            
        # User is on the Client side
            
        try:
            Issues = Issue.objects.filter(assigned_client_user=UserDetails.user_name)
        except:
            messages.error(request, "PROBLEM RETRIEVING CLIENT ISSUES!")
        
    else:
            
        # User is on the Vendor side
        
        try:
            Issues = Issue.objects.filter(assigned_vendor_user=UserDetails.user_name)
        except:
            messages.error(request, "PROBLEM RETRIEVING VENDOR ISSUES!")
  
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': Issues, 'all_clients': AllClients, 'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter })
    

"""
Get the logged in user's details re the Issue Tracking System. 
These details tells us whether the User is on the Vendor side or 
the Client side.
"""
    
def issue_tracker_user_details(request):
    
    UserDetails = ""

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
This function is called via the javascript in base.html
Get the Issues, filtered by the Issues Filter option selected
"""
def get_issues(request):
    
    data = []
    
    # Get the user's details relating to the issue tracking system - it has
    # already been established that the user's details exist, otherwise they
    # wouldnt have got this far
            
    UserDetails = issue_tracker_user_details(request)
    
    if request.method == "POST":
        
        # Get the issues from the issues database
        
        Issues = Issue.objects.all()
        
        # Get the filters - passed from the js in base.html
        
        issues_filter = request.POST.get('issuesFilter')
        status_filter = request.POST.get('statusFilter')
        client_filter = request.POST.get('clientFilter')
        
        # User is looking at all issues?
        
        if issues_filter == 'ALL ISSUES':
            
            for issue in Issues:
        
                data = get_issues_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
            
        else:
            
            # User has requested all issues assigned to them?
            
            if issues_filter == 'ASSIGNED TO ME':
                
                # Is this a Client-side user?
                
                if UserDetails.user_type == "C":
    
                    for issue in Issues:
                        if issue.assigned_client_user == UserDetails.user_name:
                            data = get_issues_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
    			
                else:
                    
                    for issue in Issues:
                        if issue.assigned_vendor_user == UserDetails.user_name:
                            data = get_issues_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
                
            else:
                
                # User has requested "Our" issues. This option is relevant to 
                # client-side users only. Get all issues for the User's client 
                # code.
                
                if issues_filter == 'OUR ISSUES ONLY':
                    
                    for issue in Issues:
                        if issue.client_code == UserDetails.vend_client_code:
                            data = get_issues_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
                            
                else:
                    
                    # User has requested "Other Clients" issues. This option is 
                    # relevant to client-side users only. Get all issues for 
                    # the clients other than the user client
                    
                    if issues_filter == "OTHER CLIENTS' ISSUES ONLY":
            
                        for issue in Issues:
                            if issue.client_code != UserDetails.vend_client_code:
                                data = get_issues_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
        	
    return JsonResponse(data, safe=False)
    
    
"""
At this point the issues have been filtered above by the Issues filter. 
This function will apply the Status and Client Filters. 
The Client Filter will always be = "ALL" for Client-Side users 
"""

def get_issues_data(UserDetails, issue, issues_filter, status_filter, client_filter, data):
    
    # Apply the status and client filters
    
    if status_filter == 'ALL':
        if client_filter == "ALL":
            
            # All Statuses, All Clients
            append_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
            
        else:
            # All Statuses, for a specific Client
            if issue.client_code == client_filter:
                append_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
                
    else:
        if issue.status == status_filter:
            if client_filter == "ALL":
                
                # A specific Status for all Clients
                append_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
                
            else:
                if issue.client_code == client_filter:
                    
                    # A specific Status for a specific Client 
                    append_data(UserDetails, issue, issues_filter, status_filter, client_filter, data)
                    
    return data
    

# Append the selected issue to the data

def append_data(UserDetails, issue, issues_filter, status_filter, client_filter, data):
    
    data.append({
        
    	"title": issue.title,
    	"details": issue.details,
    	"client_code": issue.client_code,
        "date": issue.input_date,
        "date": datetime.strftime(issue.input_date, '%d %b %y'),
    	"user": issue.user_name,
    	"assigned_client_user": issue.assigned_client_user,
    	"assigned_vendor_user": issue.assigned_vendor_user,
    	"software_component": issue.software_component,
    	"priority": issue.priority,
    	"summary": issue.summary,
    	"status": issue.status,
    	"progress": issue.progress,
    	"user_type": UserDetails.user_type,
    	"issues_filter": issues_filter,
    	"status_filter": status_filter,
    	"client_filter": client_filter
    })
    		
    return data
    