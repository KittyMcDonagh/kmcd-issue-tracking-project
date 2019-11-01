from django.shortcuts import render

# Home Page
def home(request):
    
    """ A view that renders the index page """
    
    return render(request, "home.html")
    
