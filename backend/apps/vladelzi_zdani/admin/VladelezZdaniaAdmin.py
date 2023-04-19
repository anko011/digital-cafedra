from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.vladelzi_zdani.models import TipVladelza, VladelezZdania


@admin.register(VladelezZdania)
class VladelezZdaniaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'name',
        'tip_vladelza',
        'telefon',
        'email',
    ]
    list_display_links = [
        'id',
        'name',
        'tip_vladelza',
        'telefon',
        'email',
    ]
    search_fields = [
        'id',
        'name',
        'tip_vladelza',
        'telefon',
        'email',
    ]