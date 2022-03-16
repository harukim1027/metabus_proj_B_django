from django.contrib import admin
from find_owner_board.models import FindOwnerBoard, FindOwnerBoardComment, FindOwnerBoardImage


@admin.register(FindOwnerBoard)
class FindOwnerBoardAdmin(admin.ModelAdmin):
    list_display = ["user", "title"]
    list_display_links = ["title"]
    search_fields = ["user", "title"]


@admin.register(FindOwnerBoardComment)
class FindOwnerBoardCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comment_content"]


@admin.register(FindOwnerBoardImage)
class FindOwnerBoardImageAdmin(admin.ModelAdmin):
    pass
