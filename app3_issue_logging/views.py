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

from .forms import LogNewIssueForm, UpdateIssueForm
from .forms import LogNewIssueForm, IssueCommentForm


"""
Create a view that allows a client-side user to log a new issue or edit an existing one 
depending on whether the pk is null or not. 
"""
def new_edit_issue(request, pk=None):
    
    
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracking system. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
            
    # User is on the Client side - otherwise they wouldnt be in this view. 
    # Get the Client Details.
            
    ClientDetails = get_client(request, UserDetails.vend_client_code)
        
    # Get a list of all client-side users, to be used in the Assigned User
    # dropdown list when updating an issue
        
    AssignedUsers = get_all_client_users(request, UserDetails.vend_client_code)
    
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
        
    return  render(request, 'issuelogging.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "assigned_users": AssignedUsers})


"""
Create a view that allows:
    A Vendor-side user to change the Status, Price and Assigned Vendor User of an Issue
    A Client-side user to change the Assigne Client User of an Issue
"""
def update_issue(request, pk=None):
    
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
            
        # User is on the Client side. Get the Client Details, The Issues Filter
        # values the client user can use, and the filtered Issues
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
        AssignedUsers = get_all_client_users(request, UserDetails.vend_client_code)
        
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        AssignedUsers = get_all_vendor_users(request)
    
    
    issue = get_object_or_404(Issue, pk=pk)
    
    IssueClientDetails = get_issue_client_details(request, issue)
    
    if request.method == "POST":
        
        form = UpdateIssueForm(request.POST, request.FILES, instance=issue)
        
        print("updateissuesform======================: "+str(form))
        
        if form.is_valid():
            issue = form.save()
           
            view_comments ='n'
            return redirect(issue_details, issue.pk, view_comments)
        else:
            messages.error(request, "UNABLE TO LOG ISSUE!")
            
    else:
        
        form = UpdateIssueForm(instance=issue)
    
    return  render(request, 'issueupdate.html', {'form': form, "issue": issue, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "issueclientdetails": IssueClientDetails, "assigned_users": AssignedUsers})

    

"""
Create a view that returns a single Post object based on the Post ID(pk)
and render it to the 'postdetail.html' template or return a 404 error if
the Post is not found.
"""
def issue_details(request, pk, view_comments=None, back_to_page=None, list_filters=None):
    
    print("in issue_details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
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
            
        # User is on the Client side. Get the Client Details, The Issues Filter
        # values the client user can use, and the filtered Issues
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
        
        
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
        
        IssueClientDetails = get_issue_client_details(request, issue)
       
    print("loading issuesdetails.html")
    
    return  render(request, 'issuedetails.html', {'issue': issue, 'issuecomments': issuecomments, 'view_comments': view_comments, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails, "issueclientdetails": IssueClientDetails, "back_to_page": back_to_page, "list_filters": list_filters })
    


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
Get all client-side users - needed for the 'assigned user dropdown' when editing an issue.
"""
    
def get_all_client_users(request, user_client_code):
    
    print("in get_all_client_users~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("user_client_code: "+str(user_client_code))
    
    AllClientUsers = ""

    try:
        AllClientUsers = UserDetail.objects.filter(vend_client_code = user_client_code, user_type = "C")
    except:
        messages.error(request, "Problem retrieving the all client users from Issue Tracker!")
        
    print("AllClientUsers: "+str(AllClientUsers))
    
    return AllClientUsers

"""
Get all vendor-side users - needed for the 'assigned user dropdown' when updating an issue.
"""
    
def get_all_vendor_users(request):
    
    AllVendorUsers = ""

    try:
        AllVendorUsers = UserDetail.objects.filter(user_type = "V")
    except:
        messages.error(request, "Problem retrieving the all vendor users from Issue Tracker!")
    
    return AllVendorUsers
    
    

   
"""
Get the Client details
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
these issues, and click on the chevron icon to see the details of an issue.

For Vendor-side users - This report will show a total line for each client, showing the number of issues they have  these will include those
logged by the Client, and those that they flagged as having via the 'thumbs up'. They can click the down arrow to see a list of
these issues, and click on the more icon to see the details of an issue.

This function is called via the javascript in base.html
"""
def issues_report(request):
    
    ClientDetails = ""
    VendorDetails = ""
    
    # Get the user's details from re the issue tracker. It has already
    # been confirmed at login that they exist, otherwise the user wouldnt have
    # come this far
    
    UserDetails = get_user_iss_trk_details(request)
    
    # Get the Vendor or Client Details depending on which the user is 
    # associated with
        
    if UserDetails.user_type == 'C':
            
        # User is on the Client side. Get the Client Details
            
        ClientDetails = get_client(request, UserDetails.vend_client_code)
    
    else:
            
        # User is on the Vendor side
        
        VendorDetails = get_vendor(request, UserDetails)
    
    
    # Get the 'thumbs up' records from the database, depending on user type
                    
    if UserDetails.user_type == "C":
        
        # For client-side user, get the input and flagged issues for 
        # the client the user is associated with only
        
        issuethumbsups = IssueThumbsUp.objects.filter(client_code = UserDetails.vend_client_code)
        
    else:
                    
        # For vendor-side user, get all Clients flagged issues 
                    
        issuethumbsups = IssueThumbsUp.objects.all()
    
    # Return a user message if no records found
    
    data = {}
    
    if not issuethumbsups:
        messages.error(request, "NO FLAGGED ISSUES FOUND!")
   
    # Initialise top level variables
    
    client_list = []
    clienttotals = []
    data["issues"] = []
    issues  = ""
    
    
    # Order the 'thumbs up' records by client code, then create client code list 
    
    issuethumbsups = issuethumbsups.order_by('client_code')
    
    # We just want one copy of the client code in the list
    
    prev_client = ""
     
    for item in issuethumbsups:
        if item.client_code != prev_client:
            client_list.append(item.client_code)
            prev_client = item.client_code
            
    
    # Calculate the total number of issues input and / or flagge by each client, 
    # so as to create a report by client in order of number of issues - highest to lowest
    
    client_total = []
    
    for client in client_list:
        
        total_client_issues = 0
        
        # Get the isues this client has input or thumbed up
        
        issuethumbsups = IssueThumbsUp.objects.filter(client_code = client)
        
        # Increment the number of issues input or 'thumbed up' by this client
        
        for issuethumbsup in issuethumbsups:
            total_client_issues += 1
        
        # Create a tuple list with client code and total number of issues
        
        client_total.append((client, total_client_issues))
    
    # Sort the client/total list by the total number of issues (Solution for sorting list 
    # by 2nd parameter (total number of issues) found on https://www.geeksforgeeks.org/python-list-sort/)
    
    client_total.sort(key=sortTotal, reverse = True)
    
    client_list = []
    
    for item in client_total:
        client_list.append(item[0])
        

    # Loop through the clients and loop through the issues, either input or flagged
    # by them. Create a total line per client and a line per issue
    
    for client in client_list:
        
        # Initialise client level fields
        
        nr_flagged_issues = 0
        issues = ""
        
        # Get all the thumbs up records for this client - These will be
        # issues that were input by this client, and issues that were 'thumbed up'
        # by this client
        
        issuethumbsups = IssueThumbsUp.objects.filter(client_code = client)
        
        for issuethumbsup in issuethumbsups:
    
            # Loop through the issues input or flagged by this client
            
            issue = Issue.objects.filter(id=issuethumbsup.issue_id)
        
            if not issues:
                issues = issue
                print("FIRST ISSUE.......: "+str(issues))
            else:
                issues = issues | issue
                print("SUBSEQUENT ISSUE.......: "+str(issues))
                
            nr_flagged_issues += 1
            print("NUMER FLAGGED. . . : "+str(nr_flagged_issues))
            
        # Order this client's issues and flaggeissues by priority - 1 being the most urgent 
        
        issues = issues.order_by('priority', '-id')
        
        # Create a line per issue entered or flagged by this client
        # Note that the 'client_code' field below is the client who input or 
        # flagged the issue, author is the client who originally input the issue.
        # Both codes are sometimes the same and sometimes not - as when a client
        # 'thumbs up' another client's issue
        
        for issue in issues:
            data["issues"].append({
                "id": issue.id,
                "client_code": client,
                "author": issue.client_code,
            	"software_component": issue.software_component,
            	"priority": issue.priority,
            	"summary": issue.summary,
            	"details": issue.details,
            	"status": issue.status,
            })
        
        # Get the details of the current client
        
        ThisClientDetails = get_client(request, client)
        
        # Create a total record for the current client
        
        clienttotals.append({
            "client_code": client,
            "client_name": ThisClientDetails.client_name,
            "nr_flagged_issues": nr_flagged_issues
            })
            
    
    print("FINAL SET OF ISSUES ==============================:"+str(data["issues"]))
    print("FINAL CLIENT TOTALS ==============================:"+str(clienttotals))

    # Return the user message also - set above if no issues found
    	
   
        
    return  render(request, 'issuereport.html', {"clienttotals": clienttotals, "issues": data["issues"], 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails})

"""
'sortTotal' is the key provided to 'client_total.sort'. 'client_total' is a list of 
tuples (client_code, total_client_issues). These are sorted by the amount field 
so as to create a client report in order of number of issues per client - highest to lowest.
"""

    # Sort the (client, total number of issues) list by the total amount (Solution for sorting list 
    # by second parameter (amount) found on https://www.geeksforgeeks.org/python-list-sort/)
    
def sortTotal(val): 
    return val[1]  