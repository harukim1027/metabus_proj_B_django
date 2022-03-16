from django.contrib import admin
from lost_pet_board.models import LostPetBoard, LostPetBoardComment


@admin.register(LostPetBoard)
class LostPetBoardAdmin(admin.ModelAdmin):
    list_display = ["user", "title"]
    list_display_links = ["title"]
    search_fields = ["pet_name", 'breed', 'size', "title"]


@admin.register(LostPetBoardComment)
class LostPetBoardCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment_content"]
    list_display_links = ["comment_content"]
