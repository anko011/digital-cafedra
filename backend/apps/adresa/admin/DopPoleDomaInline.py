from django.contrib import admin

from apps.adresa.models import DopPoleDoma


class DopPoleDomaInline(admin.TabularInline):
    model = DopPoleDoma
    extra = 0
    autocomplete_fields = ['name']