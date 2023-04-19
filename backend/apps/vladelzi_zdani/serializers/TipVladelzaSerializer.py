from rest_framework import serializers

from apps.vladelzi_zdani.models import TipVladelza


class TipVladelzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipVladelza
        fields = '__all__'