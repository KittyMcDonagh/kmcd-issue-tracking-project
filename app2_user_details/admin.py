from django.contrib import admin

# Import the UserDetails model created in app2_user_details/models.py

from .models import UserDetail

# Register UserDetails app so that users can be added via the admin panel.

admin.site.register(UserDetail)

