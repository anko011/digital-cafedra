from django.contrib import admin

from apps.adresa.models import DopPoleNaDome


class DopPoleNaDomeInline(admin.TabularInline):
    model = DopPoleNaDome
    extra = 0
    autocomplete_fields = ['dom', 'dop_pole_doma']