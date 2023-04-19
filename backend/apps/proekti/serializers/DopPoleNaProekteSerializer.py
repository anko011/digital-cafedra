from rest_framework import serializers

from apps.proekti.models import DopPoleNaProekte


class DopPoleNaProekteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopPoleNaProekte
        fields = '__all__'