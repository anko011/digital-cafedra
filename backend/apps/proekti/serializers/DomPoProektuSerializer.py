from rest_framework import serializers

from apps.proekti.models import DomPoProektu

class DomPoProektuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomPoProektu
        fields = '__all__'