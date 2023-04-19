from rest_framework import serializers

from apps.adresa.models import TipObecta

class TipObectaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipObecta
        fields = '__all__'