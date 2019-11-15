from django.contrib import admin


# Import models:

from .models import Issue
from .models import Comment



# Register models with admin

admin.site.register(Issue)
admin.site.register(Comment)
