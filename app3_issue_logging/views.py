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
from .forms import LogNewIssueForm


"""
Log a New Issue.
"""

def new_issue(request, pk=None):
    
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
            
       
    """
    Create a view that allows us to create or edit a view depending on 
    whether the pk is null or not. 
    """
    
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    
    if request.method == "POST":
        print("In post logic")
        form = LogNewIssueForm(request.POST, request.FILES, instance=issue)
        print("checking if form valid")
        
        if form.is_valid():
            issue = form.save()
            return redirect(issue_detail, issue.pk)
        else:
            messages.error(request, "UNABLE TO POST FORM!")
            
    else:
        form = LogNewIssueForm(instance=issue)
    
    return  render(request, 'issuelogging.html', {'form': form, 'userdetails': UserDetails, 'clientdetails': ClientDetails, 'vendordetails': VendorDetails})
    
    

"""
Create a view that returns a single Post object based on the Post ID(pk)
and render it to the 'postdetail.html' template or return a 404 error if
the Post is not found.
"""
def issue_detail(request, pk):
    
    issue = get_object_or_404(Issue, pk=pk)
    
    return  render(request, 'issuedetails.html', {'issue': issue})
    


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
The logged in user is on the Vendor side - get the Vendor details
"""
def get_vendor(request, UserDetails):
        
        try:
            VendorDetails = Vendor.objects.get(vend_code=UserDetails.vend_client_code)
        except:
            messages.error(request, "Vendor details not found!")
        
        return  VendorDetails
        
    
    