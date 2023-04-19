from rest_framework import serializers

from apps.proekti.models import ResheniePoProektu


class ResheniePoProektuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResheniePoProektu
        fields = '__all__'