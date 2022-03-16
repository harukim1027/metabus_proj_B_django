from django.contrib import admin
from adopt_assignment.models import AdoptAssignment


@admin.register(AdoptAssignment)
class AdoptAssignmentAdmin(admin.ModelAdmin):
    list_display = ["assignment_no", "user", "animal"]
    list_display_links = ["assignment_no"]
    search_fields = ["assignment_no"]

