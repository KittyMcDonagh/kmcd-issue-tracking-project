from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Only allow logged in users to access the system
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


# @login_required will first check if the user is logged in. If not they will
# be re-directed to the login page

@login_required
def logout(request):
    
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('home'))
    
    
def login(request):
    
    """ If the user is already logged in, send them back to home page """
        
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    """ If user has sent login details, validate them """
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, "Your user name or password is incorrect")
    
    else:
        
        """ Return a login page """
    
        # Set user login form = instance of UserLoginForm (see forms.py), 
        # notice the "()"" here, and display for user to log in
    
        login_form = UserLoginForm()
    
    return render(request, 'login.html', {"login_form": login_form})
    
    

# User registration view

def registration(request):
    
    """ If the user is already logged in, send them back to home page """
        
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    """ If user has sent login details, validate them """
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account at this time")
                
    else:
        registration_form = UserRegistrationForm()
    
    """ Render the registration page """
    return render(request, 'registration.html', {
        'registration_form': registration_form})


def user_profile(request):
    
    """ User's Profile page """
    
    user = User.objects.get(email=request.user.email)
    
    return render(request, 'profile.html', {'profile': user})
    
    

