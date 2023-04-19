from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.proekti.models import DopPoleProekta


@admin.register(DopPoleProekta)
class DopPoleProektaAdmin(ImportExportModelAdmin):
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
