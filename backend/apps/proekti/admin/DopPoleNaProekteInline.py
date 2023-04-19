from django.contrib import admin

from apps.proekti.models import DopPoleNaProekte

class DopPoleNaProekteInline(admin.TabularInline):
    model = DopPoleNaProekte
    extra = 0
    autocomplete_fields = ['proekt', 'dop_pole_proekta']