from django.contrib import admin

# Import the Feature model

from .models import Feature

# Register Feature model so that we can add features via the admin panel.

admin.site.register(Feature)