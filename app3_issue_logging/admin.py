from django.contrib import admin


# Import models:

from .models import Issue
from .models import IssueComment, IssueThumbsUp



# Register the above models so that they can be added via the Django Admin panel

admin.site.register(Issue)
admin.site.register(IssueComment)
admin.site.register(IssueThumbsUp)
