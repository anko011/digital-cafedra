from rest_framework import serializers

from apps.adresa.models import FotoDoma


class FotoDomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoDoma
        fields = '__all__'