from django.contrib import admin
from adopt_review.models import Review, AdoptReviewComment, AdoptReviewImage


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["review_no", "user", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]


@admin.register(AdoptReviewComment)
class AdoptReviewCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment_content"]
    list_display_links = ["comment_content"]


@admin.register(AdoptReviewImage)
class AdoptReviewImageAdmin(admin.ModelAdmin):
    list_display = ["review_image_no", "image", "review_no"]
    list_display_links = ["image"]
    search_fields = ["image", "review"]

