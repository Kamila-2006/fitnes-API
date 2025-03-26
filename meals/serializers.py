from rest_framework import serializers
from .models import Meal, MealFood


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'date', 'meal_type', 'foods']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        meal_foods = MealFood.objects.filter(workout=instance)

        representation['foods'] = [
            {
                'id': meal_food.food.id,
                'name': meal_food.food.name,
                'quantity': meal_food.quantity,
            }
            for meal_food in meal_foods
        ]
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        meal = Meal.objects.create(**validated_data)

        return meal