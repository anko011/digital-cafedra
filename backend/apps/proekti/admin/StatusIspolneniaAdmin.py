from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.proekti.models import StatusIspolnenia

@admin.register(StatusIspolnenia)
class StatusIspolneniaAdmin(ImportExportModelAdmin):
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
    save_as = True
    save_on_top = True
