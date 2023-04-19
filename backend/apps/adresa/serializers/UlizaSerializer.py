from rest_framework import serializers

from apps.adresa.models import Uliza


class UlizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uliza
        fields = '__all__'