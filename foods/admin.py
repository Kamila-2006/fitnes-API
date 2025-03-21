from django.contrib import admin
from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calories', 'protein', 'carbs', 'fats')
    search_fields = ('name',)