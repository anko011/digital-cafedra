from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.adresa.admin import FotoDomaInline, VideoDomaInline, FailDomaInline, DopPoleNaDomeInline
from apps.adresa.models import Dom


@admin.register(Dom)
class DomAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'uliza',
        'name',
        'etazhnost',
        'ploshad',
        'lat',
        'lon'
    ]
    inlines = [
        FotoDomaInline,
        VideoDomaInline,
        FailDomaInline,
        DopPoleNaDomeInline,
    ]
    autocomplete_fields = ['uliza', 'vladelez_zdania', 'zastroyshik', 'tip_obecta', 'sostoyanie_doma']
    list_display_links = [
        'id',
        'uliza',
        'name',
    ]
    search_fields = [
        'id',
        'uliza__name',
        'uliza__rayon__name',
        'name',
    ]
    list_filter = ['uliza__rayon', 'sostoyanie_doma__name', 'tip_obecta__name', 'uliza']
    save_as = True
    save_on_top = True
