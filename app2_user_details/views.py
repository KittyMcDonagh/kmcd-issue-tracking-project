from django.shortcuts import render
from django.contrib.auth.models import User

from .models import UserDetail

# User Details Page
def userpage(request):
    
    """ A view that renders the index page """
    
    
    
    return render(request, "userpage.html")
    

