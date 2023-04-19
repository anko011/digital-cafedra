from rest_framework import serializers

from apps.adresa.models import DopPoleDoma


class DopPoleDomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopPoleDoma
        fields = '__all__'