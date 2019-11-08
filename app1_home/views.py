from django.shortcuts import render
from django.contrib import messages
from accounts.forms import UserLoginForm
from app2_user_details.models import UserDetail

# Home Page
def home(request):
    
    """ A view that renders the home page """
    
    # Check whether user is logged in
    
    if request.user.is_authenticated: 
        login_form = UserLoginForm(request.POST)
    
    # User already logged in. Get the user details from the Issue Tracking System
    
        try:
            UserDetails = UserDetail.objects.get(user_name=request.user.username)
            messages.success(request, "You are already logged in!")
            return render(request, 'home.html', {'userdetails': UserDetails })
        except:
            login_form.add_error(None, "User not set up on Issue Tracking System")
        
    else:
        return render(request, "home.html")
    
