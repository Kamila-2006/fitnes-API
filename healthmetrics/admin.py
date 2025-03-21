from django.contrib import admin
from .models import HealthMetrik


@admin.register(HealthMetrik)
class HealthMetrikAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'weight', 'body_fat_percentage', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate')
    search_fields = ('user', 'date', 'weight', 'body_fat_percentage', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate')