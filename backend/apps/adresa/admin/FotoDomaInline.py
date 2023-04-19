from django.contrib import admin

from apps.adresa.models import FotoDoma


class FotoDomaInline(admin.TabularInline):
    model = FotoDoma
    extra = 0
    autocomplete_fields = ['dom']