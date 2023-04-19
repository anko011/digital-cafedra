from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.adresa.models import Rayon


@admin.register(Rayon)
class RayonAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'name',
        'naseleni_punkt',
    ]
    list_display_links = [
        'id',
        'name',
        'naseleni_punkt',
    ]
    search_fields = [
        'id',
        'name',
        'naseleni_punkt',
    ]