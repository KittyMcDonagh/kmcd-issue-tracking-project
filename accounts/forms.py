from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



# USER LOGIN FORM

class UserLoginForm(forms.Form):
    
    """ Form to be used to log user in """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



# USER REGISTRATION FORM

class UserRegistrationForm(UserCreationForm):
    
    """Form used to register a new user"""
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput)
    
    """ Create an inner class. An inner class is a class that we can use that will 
provide some information about this form. These are called meta classes and 
Django usually uses them internally to determine things about the class. 
We can also use it to specify the model that we want to store information in;
and we want we want to use it to specify the fields that we're going to expose 
which is our email, username, password1 and password2. so I'm going to copy the
name of my user registration form here and gonna head over to my views.py """

    class Meta:
        
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'email address must be unique')
            
        return email
        
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError('Please confirm your password')
            
        if password1 != password2:
            raise ValidationError('Passwords must match')
            
        return password2
        
        
        
        