from django.contrib import admin

# Import the Feature model

from .models import Feature, FeatureComment

# Register Feature model so that we can add features via the admin panel.

admin.site.register(Feature)
admin.site.register(FeatureComment)