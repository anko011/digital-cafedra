from rest_framework import serializers

from apps.proekti.models import DopPoleProekta


class DopPoleProektaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopPoleProekta
        fields = '__all__'