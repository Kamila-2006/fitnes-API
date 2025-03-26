from rest_framework import serializers
from .models import HealthMetrik


class HealthMetrikSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrik
        fields = ['id', 'date', 'weight', 'body_fat_percentage', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        health_metrik = HealthMetrik.objects.create(**validated_data)

        return health_metrik