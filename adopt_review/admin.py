from django.contrib import admin
from adopt_review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["review_no", "user", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]

