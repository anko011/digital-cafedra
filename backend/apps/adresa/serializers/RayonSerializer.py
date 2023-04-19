from rest_framework import serializers

from apps.adresa.models import Rayon


class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = '__all__'