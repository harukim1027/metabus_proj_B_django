from django.contrib import admin

from notice.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["notice_no", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]

