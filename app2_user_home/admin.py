from django.contrib import admin

"""
Import the UserDetails model, Vendor model, and Client moded created in 
 app2_user_details/models.py
"""

from .models import UserDetail
from .models import Vendor
from .models import Client

# Register UserDetails, Vendor, and Client so that they can be added via the 
# Django Admin panel.

admin.site.register(Vendor)
admin.site.register(Client)
admin.site.register(UserDetail)

