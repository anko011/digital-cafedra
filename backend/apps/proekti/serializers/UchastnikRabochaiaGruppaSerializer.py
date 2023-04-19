from rest_framework import serializers

from apps.proekti.models import UchastnikRabochaiaGruppa


class UchastnikRabochaiaGruppaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UchastnikRabochaiaGruppa
        fields = '__all__'