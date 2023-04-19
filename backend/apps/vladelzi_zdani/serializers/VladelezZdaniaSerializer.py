from rest_framework import serializers

from apps.vladelzi_zdani.models import VladelezZdania


class VladelezZdaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VladelezZdania
        fields = '__all__'