from rest_framework import serializers

from apps.adresa.models import SostoyanieDoma


class SostoyanieDomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SostoyanieDoma
        fields = '__all__'