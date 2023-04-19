from rest_framework import serializers

from apps.proekti.models import TipResheniaPoProektu


class TipResheniaPoProektuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipResheniaPoProektu
        fields = '__all__'