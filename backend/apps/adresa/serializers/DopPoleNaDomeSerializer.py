from rest_framework import serializers

from apps.adresa.models import DopPoleNaDome


class DopPoleNaDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopPoleNaDome
        fields = '__all__'