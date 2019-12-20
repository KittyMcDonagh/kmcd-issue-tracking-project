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
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    
    print(request.method)
    
    if request.method == "POST":
        
        print("request is post-----------------------------------------")
        
        form = LogNewIssueForm(request.POST, request.FILES, instance=issue)
        
        if form.is_valid():
            print("form is valid")
        
            issue = form.save()
            
            print("form.priority: "+str(form))
            
            view_comments = 'n'
            return redirect(issue_details, issue.pk, view_comments)
        else:
            print("form.priority: "+str(form))
            messages.error(request, "UNABLE TO LOG ISSUE!")
            
    else:
        print("request is get-----------------------------------------")
        print("issue: "+str(issue))
        form = LogNewIssueForm(instance=issue)
    
    return  render(request, 'issuelogging.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails})


"""
Create a view that allows a vendor-side user to change the status of an issue. 
"""
def update_issue_status_priority(request, pk=None):
    
    print("UPDATE STATUS ------------------------------------------")
    
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
    
    print(request.method)
    
    if request.method == "POST":
        
        print("request is post-----------------------------------------")
        
        form = IssueStatusPriorityForm(request.POST, request.FILES, instance=issue)
        
        if form.is_valid():
            print("form is valid")
        
            issue = form.save()
            
            print("form.priority: "+str(form))
            
            view_comments ='n'
            return redirect(issue_details, issue.pk, view_comments)
        else:
            print("form.priority: "+str(form))
            messages.error(request, "UNABLE TO LOG ISSUE!")
            
    else:
        print("request is get-----------------------------------------")
        print("issue: "+str(issue))
        form = IssueStatusPriorityForm(instance=issue)
    
    return  render(request, 'issuestatuspriority.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "issueclientdetails": IssueClientDetails})

    

"""
Create a view that returns a single Post object based on the Post ID(pk)
and render it to the 'postdetail.html' template or return a 404 error if
the Post is not found.
"""
def issue_details(request, pk, view_comments=None):
    
    print("IN ISSUE DETAILS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    # Is user requesting to view the comments?
    
    print("VIEW_COMMENTS: "+str(view_comments))
    
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
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        IssueClientDetails = get_issue_client_details(request, issue)
        
    print("issue: "+str(issue.id))
    print("view_comments: "+str(view_comments))
    print("issue: "+str(issue))
    print("comments: "+str(issuecomments))
    
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

def get_client(request, UserDetails):

    try:
        ClientDetails = Client.objects.get(client_code=UserDetails.vend_client_code)
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
            
        ClientDetails = get_client(request, UserDetails)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    # Get the issue for which the comment is being input
    
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    
    pk = ""
    
    issuecomment = get_object_or_404(Issue, pk=pk) if pk else None
    
    print(request.method)
    
    comments_input = "n"
    view_comments = 'n'
    
    if request.method == "POST":
        
        print("issue comment request is post----------------------------------")
        
        form = IssueCommentForm(request.POST, request.FILES, instance=issuecomment)
        
        if form.is_valid():
            print("comment form is valid. form = "+str(form))
        
            issuecomment = form.save()
            
            print("ISSUECOMMENT.ISSUE_ID"+str(issuecomment.issue_id))
            
            # Redirect to issue_details and pass 'y' to let issuedetails.html
            # know that the comments list is to be displayed
            
            view_comments = 'y'
            
            return redirect(issue_details, issuecomment.issue_id, view_comments)
        else:
        
            print("form invalid = "+str(form))
            messages.error(request, "UNABLE TO LOG ISSUE COMMENT!")
            
    else:
        print("issue comment request is get-----------------------------------")
    
        form = IssueCommentForm()
        
        # Set comments_input to keep the comment form fields open in issuedetails.html
    
        comments_input = "y"
        
        # Set view_comments so that the comments list wont be displayedin issuedetails.html
        
        view_comments = 'n'
        
        print("comments_input= "+str(comments_input))
    
    return  render(request, 'issuedetails.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "comments_input": comments_input, "view_comments": view_comments })
    