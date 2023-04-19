from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.proekti.admin import ResheniePoProektuInline, UchastnikRabochaiaGruppaInline, DopPoleNaProekteInline
from apps.proekti.models import Proekt

@admin.register(Proekt)
class ProektAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'vnutrinii_nomer',
        'data_nachala_proekta',
        'primechanie',
    ]
    inlines = [
        ResheniePoProektuInline,
        UchastnikRabochaiaGruppaInline,
        DopPoleNaProekteInline
    ]
    list_display_links = [
        'id',
        'vnutrinii_nomer',
        'data_nachala_proekta',
        'primechanie',
    ]
    search_fields = [
        'id',
        'vnutrinii_nomer',
        'data_nachala_proekta',
    ]
    list_filter = ['data_nachala_proekta']
    save_as = True
    save_on_top = True
