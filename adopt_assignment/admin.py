from django.contrib import admin
from adopt_assignment.models import AdoptAssignment, AdoptAssignmentHomeImage


@admin.register(AdoptAssignment)
class AdoptAssignmentAdmin(admin.ModelAdmin):
    list_display = ["assignment_no", "user", "animal"]
    list_display_links = ["assignment_no"]
    search_fields = ["assignment_no"]




@admin.register(AdoptAssignmentHomeImage)
class AdoptAssignmentHomeImageAdmin(admin.ModelAdmin):
    list_display = ["home_image_no"]
    list_display_links = ["home_image_no"]

