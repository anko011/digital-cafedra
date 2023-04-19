from django.contrib import admin

from apps.proekti.models import ResheniePoProektu

class ResheniePoProektuInline(admin.TabularInline):
    model = ResheniePoProektu
    extra = 0
    autocomplete_fields = ['proekt', 'dom', 'tip_reshenia_po_proektu',]