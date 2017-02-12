from django.contrib import admin
from fixit.models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'location_bdg', 'location_detail', 'upvotes', 'images')

# Register your models here.

admin.site.register(Issue, IssueAdmin)
