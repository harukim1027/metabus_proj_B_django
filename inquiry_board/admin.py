from django.contrib import admin
from inquiry_board.models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ["user", "title"]
    list_display_links = ["title"]
    search_fields = ["user", "title"]

