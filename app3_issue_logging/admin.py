from django.contrib import admin


# Import models:

from .models import Issue
from .models import VendorComment
from .models import FilterForVendUser
from .models import FilterForClientUser
from .models import StatusFilter


# Register models with admin

admin.site.register(Issue)
admin.site.register(VendorComment)
admin.site.register(FilterForVendUser)
admin.site.register(FilterForClientUser)
admin.site.register(StatusFilter)