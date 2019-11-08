from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

from .models import UserDetail

from accounts.forms import UserLoginForm

# User Home Page
def userhome(request):
    
    """
    The accounts login has already verified that this user is set up on the 
    Issue Tracking System. Retrieve the details here again before going to the
    User's home page
    """
    
    UserDetails = UserDetail.objects.get(user_name=request.user.username)
        
    
    return render(request, 'userhome.html', {'userdetails': UserDetails })
    

