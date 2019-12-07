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

    # Get all issues
    
    Issues = ""
    
    # Get the issues assigned to the logged only. 
    # An issue can be assigned both to a client-side user and a vendor-side user, 
    # so we need to verify which one it is
    
    if UserDetails.user_type == "C":
            
        # User is on the Client side
                
        try:
            Issues = Issue.objects.filter(assigned_client_user=UserDetails.user_id)
        except:
            messages.error(request, "PROBLEM RETRIEVING ISSUES!")
            
    else:
                
        # User is on the Vendor side
            
        try:
            Issues = Issue.objects.filter(assigned_vendor_user=UserDetails.user_id)
        except:
            messages.error(request, "PROBLEM RETRIEVING ISSUES!")
                
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Issues = FinalFilterIssues(request, Issues, UserDetails)

    # For Pagination
    
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
  
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': issues, 'all_clients': AllClients, 'selected_issues_filter':SelectedIssuesFilter, 'selected_status_filter': SelectedStatusFilter, 'selected_priority_filter': SelectedPriorityFilter, 'selected_client_filter': SelectedClientFilter, "listing":listing, "list_type": list_type })


"""
User Home Page - Get all issues
All issues are shown.
"""

def get_all_issues(request):
    
    
    SelectedIssuesFilter = "ALL"
    
    # Set Client Filter to ALL
        
    SelectedClientFilter = "ALL"
    
    # set Status Filter to ALL
    
    SelectedStatusFilter = "ALL"
    
    # set Status Filter to ALL
    
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
            
        # User is on the Client side. Get the Client Details, The Issues Filter
        # values the client user can use, and the filtered issues
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
            
        # Get all clients for Client Dropdown - only available to Vendor-side 
        # users
            
        AllClients = get_all_clients(request)
        

    # Get all issues
    
    Issues = Issue.objects.all()
    
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Issues = FinalFilterIssues(request, Issues, UserDetails)

    # For Pagination
    
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
  
    return render(request, 'userhome.html', {'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, 'issues': issues, 'all_clients': AllClients, 'selected_issues_filter':SelectedIssuesFilter, 'selected_client_filter': SelectedClientFilter, 'selected_status_filter': SelectedStatusFilter, "selected_priority_filter": SelectedPriorityFilter, "listing":listing })



"""
This function is called via the javascript in base.html
Get the issues, filtered by the issues Filter option selected
"""
def get_issues(request):
    
    print("in get_issues ------------------------------------------>")
    
    data = []
    
    # Get the user's details relating to the Issue Tracker app - it has
    # already been established that the user's details exist, otherwise they
    # wouldnt have got this far
            
    UserDetails = get_user_iss_trk_details(request)
        
    # Get all the issues from the issues database
        
    Issues = Issue.objects.all()
    
    # Get the filters - passed from the js in base.html
        
    issues_filter = request.POST.get('issuesFilter')
    status_filter = request.POST.get('statusFilter')
    priority_filter = request.POST.get('priorityFilter')
    client_filter = request.POST.get('clientFilter')
    
    print("issues_filter: "+str(issues_filter))
    print("status_filter: "+str(status_filter))
    print("priority_filter: "+str(priority_filter))
    print("client_filter: "+str(client_filter))
    
    print("STILL in get_issues ------------------------------------------>")
    
    
    # User has requested all issues assigned to them?
            
    if issues_filter == 'ASSIGNED TO ME':
                
        # Is this a Client-side user?
                
        if UserDetails.user_type == "C":
    
            Issues = Issues.filter(assigned_client_user = UserDetails.user_id)
    			
        else:
                
            # This is a Vendor-side user
                
            Issues = Issues.filter(assigned_vendor_user = UserDetails.user_id)
                
    else:
                
        # Has user requested 'Our Issues Only'?
        # This option is relevant to Client-side users only'
                
        if issues_filter == 'OUR ISSUES ONLY':
                    
            Issues = Issues.filter(client_code = UserDetails.vend_client_code)
                            
        else:
                    
            # Has user requested 'Other Clients' issues Only?
                
            if issues_filter == "OTHER CLIENTS' ISSUES ONLY":
            
                Issues = Issues.exclude(client_code = UserDetails.vend_client_code)
        
    # Filter issues further if status filter is set . . .
        
    if status_filter != "ALL":
        Issues = Issues.filter(status=status_filter)
        
    # . . . or if Client filter is set (client filter is availabe to vendor
    # -side users only)
        
    if client_filter != "ALL":
        Issues = Issues.filter(client_code=client_filter)
        
    # . . . or if Priority filter is set 
    
    print("Before filtering by priority: priority_filter "+str(priority_filter))
        
    if priority_filter != "ALL":
        Issues = Issues.filter(priority=priority_filter)
        
    print("After filtering by priority: priority_filter "+str(priority_filter))
        
    
    # Final filtering is done here to make sure users only see what they're
    # allowed to see, and they're sorted by date, descending
    
    Issues = FinalFilterIssues(request, Issues, UserDetails)
    
    user_message = ""
    
    if not Issues:
        user_message = "No issues found for the selected criteria!"
    
    print("user_message: "+str(user_message))

    # For Pagination
    
    print("request.method: "+str(request.method))
    
    page = request.POST.get('page', 1)
    
    print("page = "+str(page))
    
    paginator = Paginator(Issues, 5)
    
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        issues = paginator.page(1)
    except EmptyPage:
        issues = paginator.page(paginator.num_pages)
        
    # Save the pagination parameters for use in the js function in base.html
    # that called 'get_issues'
        
    has_other_pages = issues.has_other_pages()
    has_prev_page = issues.has_previous()
    current_page = issues.number
    has_next_page = issues.has_next()
    
    prev_page_nr = 0
    if issues.has_previous():
        prev_page_nr = issues.previous_page_number()
        
    next_page_nr = 0
    if issues.has_next():
        next_page_nr = issues.next_page_number()
        
    page_range = paginator.page_range
    
    # Create data dictionary to return to the js function (in base.html)
    
    data = {}

    # Return the pagination parameters for output to the html file
    
    data["pagination_props"] = {
		"has_other_pages": has_other_pages,
		"has_prev_page": has_prev_page,
		"current_page": current_page,
		"has_next_page": has_next_page,
		"prev_page_nr": prev_page_nr,
		"next_page_nr": next_page_nr,
		"page_range": list(page_range)
	}
	
	# Return the user message also - set above if no issues found
	
    data["user_mesg"] = {
        
        "user_message": user_message
	  }
	
	# Return the issues to be output to  the html table
	
    data["issues"] = []
   
    for issue in issues:
        data["issues"].append({
            
            "id": issue.id,
        	"title": issue.title,
        	"details": issue.details,
        	"client_code": issue.client_code,
            "date": datetime.strftime(issue.input_date, '%d %b %y'),
        	"user": issue.user_id,
        	"assigned_client_user": issue.assigned_client_user,
        	"assigned_vendor_user": issue.assigned_vendor_user,
        	"software_component": issue.software_component,
        	"priority": issue.priority,
        	"summary": issue.summary,
        	"status": issue.status,
        	"user_type": UserDetails.user_type
    })
    
    return JsonResponse(data, safe=False)
    
"""
Final filter to make sure users see only what they're allowed to see.
Vendors can only see issues when they reach status of 'LOGGED' (i.e. they cannot
see 'DRAFT')
Clients cannot see issues of other clients that are of status 'DRAFT' or 'LOGGED'
"""

def FinalFilterIssues(request, Issues, UserDetails):
    
    if UserDetails.user_type == "V":
        
        # This is a Vendor-side user
        # Vendors cannot see issues until they reach status 'LOGGED'
                
        Issues = Issues.exclude(status = "DRAFT")
    
    else:
        
        # Client-side users cannot see issues of other clients that are still
        # at status 'DRAFT' or 'LOGGED'
        
        # Separating our clients from other clients, so that I can filter other 
        # clients issues by status
        
        OurClientsIssues = Issues.filter(client_code = UserDetails.vend_client_code)
        
        OtherClientsIssues = Issues.exclude(client_code = UserDetails.vend_client_code)
        OtherClientsIssues = OtherClientsIssues.exclude(status = "DRAFT").exclude(status = "LOGGED")
        
        # Putting the two lists together after filtering other clients issues
        
        Issues = OurClientsIssues | OtherClientsIssues
    
    # Sorting issues by date, descending order
        
    Issues = Issues.order_by('-input_date')
        
    return Issues
        


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