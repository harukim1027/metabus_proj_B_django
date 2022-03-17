from django.contrib import admin
from around_infra.models import AroundInfra, InfraCategory


@admin.register(AroundInfra)
class AroundInfraAdmin(admin.ModelAdmin):
    list_display = ["infra_name", "infra_address", "infra_call"]
    list_display_links = ["infra_name"]
    search_fields = ["infra_name"]



@admin.register(InfraCategory)
class InfraCategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]
    list_display_links = ["category_name"]
