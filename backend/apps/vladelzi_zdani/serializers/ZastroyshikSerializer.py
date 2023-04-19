from rest_framework import serializers

from apps.vladelzi_zdani.models import Zastroyshik


class ZastroyshikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zastroyshik
        fields = '__all__'