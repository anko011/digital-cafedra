from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.vladelzi_zdani.models import Zastroyshik


@admin.register(Zastroyshik)
class ZastroyshikAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    list_display_links = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]