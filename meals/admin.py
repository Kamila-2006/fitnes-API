from django.contrib import admin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'meal_type')
    search_fields = ('user', 'date', 'meal_type')