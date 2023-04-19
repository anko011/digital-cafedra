from django.contrib import admin

from apps.proekti.models import DopPoleProekta


class DopPoleProektaInline(admin.TabularInline):
    model = DopPoleProekta
    extra = 0
    autocomplete_fields = ['name']