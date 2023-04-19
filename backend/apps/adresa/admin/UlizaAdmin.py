from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.adresa.models import  Uliza


@admin.register(Uliza)
class UlizaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'rayon',
        'name',
    ]
    autocomplete_fields = ['rayon']
    list_display_links = [
        'id',
        'rayon',
        'name',
    ]
    search_fields = [
        'id',
        'rayon__name',
    ]
    list_filter = ['rayon']