from django.contrib import admin
from streetanimal.models import Animal, AllSecurityCenter

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["announce_no", "breed", "color", "sex"]
    list_display_links = ["announce_no"]
    search_fields = ["announce_no"]


@admin.register(AllSecurityCenter)
class CenterAdmin(admin.ModelAdmin):
    list_display = ["center_name"]
    list_display_links = ["center_name"]
    search_fields = ["center_name"]


