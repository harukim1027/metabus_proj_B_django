from django.contrib import admin

from notice.models import Notice, NoticeFile, NoticeImage


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["notice_no", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]



@admin.register(NoticeFile)
class NoticeFileAdmin(admin.ModelAdmin):
    list_display = ["notice_file_no"]
    list_display_links = ["notice_file_no"]


@admin.register(NoticeImage)
class NoticeImageAdmin(admin.ModelAdmin):
    list_display = ["notice_image_no"]
    list_display_links = ["notice_image_no"]


