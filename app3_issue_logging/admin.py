from django.contrib import admin


# Import models:

from .models import Issue
from .models import VendorComment
from .models import FilterForVendor
from .models import FilterForClient
from .models import StatusFilter


# Register models with admin

admin.site.register(Issue)
admin.site.register(VendorComment)
admin.site.register(FilterForVendor)
admin.site.register(FilterForClient)
admin.site.register(StatusFilter)