from django.contrib import admin

from apps.adresa.models import FotoDoma, VideoDoma


class VideoDomaInline(admin.TabularInline):
    model = VideoDoma
    extra = 0
    autocomplete_fields = ['dom']