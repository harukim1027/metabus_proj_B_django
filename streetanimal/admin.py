from django.contrib import admin
from streetanimal.models import Animal, AnimalImage


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["animal_no", "animal_reg_num", "category", "size", "sex", "protection_status"]
    list_display_links = ["animal_reg_num"]
    search_fields = ["animal_reg_num"]


@admin.register(AnimalImage)
class AnimalImageAdmin(admin.ModelAdmin):
    pass