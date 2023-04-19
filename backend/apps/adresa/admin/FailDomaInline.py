from django.contrib import admin

from apps.adresa.models import FailDoma


class FailDomaInline(admin.TabularInline):
    model = FailDoma
    extra = 0
    autocomplete_fields = ['dom']