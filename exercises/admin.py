from django.contrib import admin
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'calories_burned_per_hour')
    search_fields = ('name', 'description', 'category')