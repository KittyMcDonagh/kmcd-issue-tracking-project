from django.contrib import admin


# Import models:

from .models import Issue
from .models import IssueComment, IssueThumbsUp



# Register models with admin

admin.site.register(Issue)
admin.site.register(IssueComment)
admin.site.register(IssueThumbsUp)
