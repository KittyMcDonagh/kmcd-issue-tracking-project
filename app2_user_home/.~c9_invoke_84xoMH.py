from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def user_home(request):
    
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
            messages.error(request, "PROBLEM RETRIEVING ISSUES!")
        
    else:
            
        # User is on the Vendor side
        
        try:
            Issues = Issue.objects.filter(assigned_vendor_user=UserDetails.user_name)
        except:
            messages.error(request, "PROBLEM RETRIEVING ISSUES!")
            
    # For Pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(Issues, 3)
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
  
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': issues, 'all_clients': AllClients, 'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter })



"""
This function is called via the javascript in base.html
Get the Issues, filtered by the Issues Filter option selected
"""
def get_issues(request):
    
    data = []
    
    # Get the user's details relating to the issue tracking system - it has
    # already been established that the user's details exist, otherwise they
    # wouldnt have got this far
            
    UserDetails = get_user_iss_trk_details(request)
    
    if request.method == "POST":
        
        # Get all the issues from the issues database
        
        Issues = Issue.objects.all()
        
        # Get the filters - passed from the js in base.html
        
        issues_filter = request.POST.get('issuesFilter')
        status_filter = request.POST.get('statusFilter')
        client_filter = request.POST.get('clientFilter')
        
        print("issues_filter: "+issues_filter)
       
        
        
        # User has requested all issues assigned to them?
            
        if issues_filter == 'ASSIGNED TO ME':
                
            # Is this a Client-side user?
                
            if UserDetails.user_type == "C":
    
                Issues = Issues.filter(assigned_client_user = UserDetails.user_name)
    			
            else:
                
                # This is a Vendor-side user
                
                Issues = Issues.filter(assigned_vendor_user = UserDetails.user_name)
                
        else:
                
            # Has user requested 'Our Issues Only?
            # This option is relevant to Client-side users only'
                
            if issues_filter == 'OUR ISSUES ONLY':
                    
                Issues = Issues.filter(client_code = UserDetails.vend_client_code)
                            
            else:
                    
                # Has user requested 'Other Clients' Issues Only?
                # This option is relevant to Client-side users only'
                    
                if issues_filter == "OTHER CLIENTS' ISSUES ONLY":
            
                    Issues = Issues.exclude(client_code = UserDetails.vend_client_code)
        
        # Filter issues further if status filter is set . . .
        
        if status_filter != "ALL":
            print("status_filter: "+status_filter)
            Issues = Issues.filter(status=status_filter)
        
        # . . . or if Client filter is set (client filter is availabe to vendor
        # -side users only)
        
        if client_filter != "ALL":
            print("client_filter: "+client_filter)
            Issues = Issues.filter(client_code=client_filter)
            
    # For Pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(Issues, 3)
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
                    
    
    for issue in issues:
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
    })
    
    page_nav = []
    
    page_nav.append({
        "has_previous": issues.has_previous,
        "previous_page_number": issues.previous_page_number,
        "page_range": issues.paginator.page_range,
        "has_next": issues.has_next
        
    })
    
    issues = data
    
    
        	
    return JsonResponse(issues, page_nav, safe=False)




"""
Get the logged in user's details re the Issue Tracking System. 
These details tells us whether the User is on the Vendor side or 
the Client side.
"""
    
def get_user_iss_trk_details(request):
    
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










