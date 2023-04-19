from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.adresa.models import DopPoleDoma


@admin.register(DopPoleDoma)
class DopPoleDomaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    list_display_links = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
    save_as = True
    save_on_top = True
