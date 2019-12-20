from django.contrib import admin

# Import the Feature model

from .models import Feature, FeatureComment, FeaturePaid

# Register the Features models so that we can access them via the admin panel.

admin.site.register(Feature)
admin.site.register(FeatureComment)
admin.site.register(FeaturePaid)