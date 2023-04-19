from rest_framework import serializers

from apps.adresa.models import NaseleniPunkt


class NaseleniPunktSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaseleniPunkt
        fields = '__all__'