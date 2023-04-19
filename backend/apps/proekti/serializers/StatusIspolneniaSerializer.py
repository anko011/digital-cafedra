from rest_framework import serializers

from apps.proekti.models import StatusIspolnenia


class StatusIspolneniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusIspolnenia
        fields = '__all__'