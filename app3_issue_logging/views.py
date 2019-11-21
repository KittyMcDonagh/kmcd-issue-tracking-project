from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import HttpResponse
from django.http import JsonResponse 

from datetime import datetime

from app2_user_home.models import Vendor
from app2_user_home.models import Client
from app2_user_home.models import UserDetail

from .models import Issue




"""
Enter a New Issue.
"""

def new_issue(request):
    
    
            
  
    return render(request, 'issue-logging.html')