from django.contrib import admin
from streetanimal.models import Animal, All_security_center, Animal_image


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["announce_no", "breed", "color", "sex", "age", "status"]
    list_display_links = ["announce_no"]
    search_fields = ["announce_no"]


@admin.register(All_security_center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ["center_name"]
    list_display_links = ["center_name"]
    search_fields = ["center_name"]

@admin.register(Animal_image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["image1"]
    list_display_links = ["image1"]
    search_fields = ["image1"]
