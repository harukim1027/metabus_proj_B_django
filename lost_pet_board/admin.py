from django.contrib import admin
from lost_pet_board.models import LostPetBoard, LostPetBoardComment, LostPetBoardImage


@admin.register(LostPetBoard)
class LostPetBoardAdmin(admin.ModelAdmin):
    list_display = ["lost_board_no", "user", "title"]
    list_display_links = ["title"]
    search_fields = ["pet_name", 'breed', "title"]


@admin.register(LostPetBoardComment)
class LostPetBoardCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment_content"]
    list_display_links = ["comment_content"]


@admin.register(LostPetBoardImage)
class LostPetBoardImageAdmin(admin.ModelAdmin):
    list_display = ["lost_image_no"]
    list_display_links = ["lost_image_no"]

