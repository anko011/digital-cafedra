from django.contrib import admin

from apps.proekti.models import UchastnikRabochaiaGruppa


class UchastnikRabochaiaGruppaInline(admin.TabularInline):
    model = UchastnikRabochaiaGruppa
    extra = 0
    autocomplete_fields = ['proekt', 'user']