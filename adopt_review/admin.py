from django.contrib import admin
from adopt_review.models import Review,AdoptReviewComment


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["review_no", "user", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]



@admin.register(AdoptReviewComment)
class AdoptReviewCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment_content"]
    list_display_links = ["comment_content"]
