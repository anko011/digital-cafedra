from rest_framework import serializers

from apps.adresa.models import VideoDoma


class VideoDomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDoma
        fields = '__all__'