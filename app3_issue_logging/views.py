from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import HttpResponse
from django.http import JsonResponse 

from datetime import datetime

from app2_user_home.models import Vendor
from app2_user_home.models import Client
from app2_user_home.models import UserDetail

from .models import Issue
from .models import IssueComment, IssueThumbsUp

from .forms import LogNewIssueForm, IssueStatusPriorityForm
from .forms import LogNewIssueForm, IssueCommentForm


"""
Create a view that allows us to log a new issue or edit an existing one 
depending on whether the pk is null or not. 
"""
def new_edit_issue(request, pk=None):
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
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
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    
    if request.method == "POST":
        
        form = LogNewIssueForm(request.POST, request.FILES, instance=issue)
        
        if form.is_valid():
            issue = form.save()
            
            # Create a 'thumbs up' record for this client / issue, but make the 'thumbs_up' field = '0'
            # A client will not be able to 'thumbs up' their own issues, and we want to distinguish issues a
            # client input, from ones they 'thumbed up' (i.e. saying 'I have this too.')
            
            issue_thumbs_up, _ = IssueThumbsUp.objects.get_or_create(issue_id=issue.id, client_code=UserDetails.vend_client_code, defaults={"author":issue.client_code, "user_id":UserDetails.user_id, "thumbs_up": 0})
            
            view_comments = 'n'
            return redirect(issue_details, issue.pk, view_comments)
        else:
            
            messages.error(request, "UNABLE TO LOG ISSUE!")
            
    else:
        
        form = LogNewIssueForm(instance=issue)
    
    return  render(request, 'issuelogging.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails})


"""
Create a view that allows a vendor-side user to change the status of an issue. 
"""
def update_issue_status_priority(request, pk=None):
    
    # This view is for vendor-side users only
    
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracking system. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # User is on the Vendor side
        
    VendorDetails = get_vendor(request, UserDetails)
    
    issue = get_object_or_404(Issue, pk=pk)
    
    IssueClientDetails = get_issue_client_details(request, issue)
    
    if request.method == "POST":
        
        form = IssueStatusPriorityForm(request.POST, request.FILES, instance=issue)
        
        if form.is_valid():
            issue = form.save()
           
            view_comments ='n'
            return redirect(issue_details, issue.pk, view_comments)
        else:
            messages.error(request, "UNABLE TO LOG ISSUE!")
            
    else:
        
        form = IssueStatusPriorityForm(instance=issue)
    
    return  render(request, 'issuestatuspriority.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "issueclientdetails": IssueClientDetails})

    

"""
Create a view that returns a single Post object based on the Post ID(pk)
and render it to the 'postdetail.html' template or return a 404 error if
the Post is not found.
"""
def issue_details(request, pk, view_comments=None):
    
    # Retrieve the issue
    
    issue = get_object_or_404(Issue, pk=pk)
    
    # Get this issue's comments 
    
    try:
        issuecomments = IssueComment.objects.filter(issue_id=issue.id)
    except:
        messages.error(request, "No comments for this Issue yet")
        
    # List the issue comments in reverse input order
        
    issuecomments = issuecomments.order_by('-id')
    
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
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details, The Issues Filte
        # values the client user can use, and the filtered Issues
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        IssueClientDetails = get_issue_client_details(request, issue)
    
    return  render(request, 'issuedetails.html', {'issue': issue, 'issuecomments': issuecomments, 'view_comments': view_comments, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "issueclientdetails": IssueClientDetails})
    


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

def get_client(request, get_client_code):

    try:
        ClientDetails = Client.objects.get(client_code=get_client_code)
    except:
        messages.error(request, "Client details not found!")
   
    return  ClientDetails
    
    
    
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
Get the details of the Client the issue belongs to. This is required for a Vendor
user only. Although Client-side users see other clients' issues, they dont see
the details of those clients.
"""
def get_issue_client_details(request, issue):
    
    IssueClientDetails = ""

    try:
        IssueClientDetails = Client.objects.get(client_code=issue.client_code)
    except:
        messages.error(request, "Issue Client details not found!")
        
    return IssueClientDetails
        

"""
New Issue comment - get the issue comments form. This view is called when the user
clicks '+' to add a comment. The id of the issue is passed to the view
"""
def new_issue_comment(request, pk=None):
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
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
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    # Get the issue for which the comment is being input
    
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    
    pk = ""
    
    issuecomment = get_object_or_404(Issue, pk=pk) if pk else None
   
    comments_input = "n"
    view_comments = 'n'
    
    if request.method == "POST":
        
        form = IssueCommentForm(request.POST, request.FILES, instance=issuecomment)
        
        if form.is_valid():
            issuecomment = form.save()
            
            # Redirect to issue_details and pass 'y' to let issuedetails.html
            # know that the comments list is to be displayed
            
            view_comments = 'y'
            
            return redirect(issue_details, issuecomment.issue_id, view_comments)
        else:
            messages.error(request, "UNABLE TO LOG ISSUE COMMENT!")
            
    else:
        
        form = IssueCommentForm()
        
        # Set comments_input to keep the comment form fields open in issuedetails.html
    
        comments_input = "y"
        
        # Set view_comments so that the comments list wont be displayedin issuedetails.html
        
        view_comments = 'n'
        
    return  render(request, 'issuedetails.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "comments_input": comments_input, "view_comments": view_comments })


"""
ISSUES REPORT - 
For Client-side users - This report will show a total line of the number of issues the Client has - these will include those
logged by this Client, and those that they flagged as having via the 'thumbs up'. They can click the down arrow to see a list of
these issues, and click on the more icon to see the details of an issue.

For Vendor-side users - This report will show a total line for each client, showing the number of issues they have  these will include those
logged by the Client, and those that they flagged as having via the 'thumbs up'. They can click the down arrow to see a list of
these issues, and click on the more icon to see the details of an issue.

This function is called via the javascript in base.html
"""
def issues_report(request):
    
    # If the user is on the Client side we need the Client details, otherwise
    # we need the Vendor details
    
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
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    # Is this a Client-side user?
                    
    if UserDetails.user_type == "C":
        
        # For client-side user, get this Clients flagged issues only
        
        issuethumbsups = IssueThumbsUp.objects.filter(client_code = UserDetails.vend_client_code)
        issuethumbsups = issuethumbsups.order_by('client_code', '-issue_id')
        
    else:
                    
        # For vendor-side user, get this Clients flagged issues only
                    
        issuethumbsups = IssueThumbsUp.objects.all()
        issuethumbsups = issuethumbsups.order_by('client_code', '-issue_id')
        
    user_message = ""
    
    if not issuethumbsups:
        user_message = "No flagged issues found!"

    # Create data dictionary to return to the js function (in base.html)
        
    data = {}
        
    # Return the user message also - set above if no issues found
    	
    data["user_mesg"] = {
            
        "user_message": user_message
    }
    	
    # Return the issues to be output to  the html table
    	
    data["issues"] = []
    nr_flagged_issues = 0
    prev_client = ""
    clienttotal = []
    
    client_list = []
    prev_client = ""
    i = 0
        
    for item in issuethumbsups:
        if item.client_code != prev_client:
            client_list.append(item.client_code)
            prev_client = item.client_code
    
    for client in client_list:
        
        issuethumbsups = IssueThumbsUp.objects.filter(client_code = client)
        
        i = 0
        
        for issuethumbsup in issuethumbsups:
    
            # Loop through the issues for this client
            
            issue = Issue.objects.get(client_code = issuethumbsup.author, id=issuethumbsup.issue_id)
        
            nr_flagged_issues+=1
            
            data["issues"].append({
                "id": issue.id,
                "client_code": issuethumbsup.client_code,
                "author": issue.client_code,
            	"software_component": issue.software_component,
            	"priority": issue.priority,
            	"summary": issue.summary,
            	"details": issue.details,
            	"status": issue.status,
            })
        
        ThisClientDetails = get_client(request, client)
        
        clienttotal.append({
            "client_code": client,
            "client_name": ThisClientDetails.client_name,
            "nr_flagged_issues": nr_flagged_issues
            })
        nr_flagged_issues = 0
        
    return  render(request, 'issuereport.html', {"clienttotal": clienttotal, "issues": data["issues"], 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails})

