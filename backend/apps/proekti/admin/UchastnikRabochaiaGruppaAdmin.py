from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.proekti.models import UchastnikRabochaiaGruppa


@admin.register(UchastnikRabochaiaGruppa)
class UchastnikRabochaiaGruppaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'proekt',
        'fio_uchastnika_gruppi',
        'dolznost_uchastnika_gruppi',
        'user',
    ]
    autocomplete_fields = ['proekt', 'user']
    list_display_links = [
        'id',
        'proekt',
        'fio_uchastnika_gruppi',
        'dolznost_uchastnika_gruppi',
        'user',
    ]
    search_fields = [
        'id',
        'proekt',
        'fio_uchastnika_gruppi',
        'dolznost_uchastnika_gruppi',
        'user',
    ]
    list_filter = [
        'proekt'
    ]
    save_as = True
    save_on_top = True
