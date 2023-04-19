from rest_framework import serializers

from apps.adresa.models import Okrug


class OkrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okrug
        fields = '__all__'