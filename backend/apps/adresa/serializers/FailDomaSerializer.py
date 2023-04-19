from rest_framework import serializers

from apps.adresa.models import FailDoma

class FailDomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailDoma
        fields = '__all__'