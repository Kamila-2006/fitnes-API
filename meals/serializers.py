from rest_framework import serializers
from .models import Meal, MealFood
from foods.models import Food


class MealSerializer(serializers.ModelSerializer):
    foods = serializers.ListSerializer(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'date', 'meal_type', 'foods']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        meal_foods = MealFood.objects.filter(meal=instance)

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
        foods_data = validated_data.pop('foods', [])
        meal = Meal.objects.create(user=user, **validated_data)

        for item in foods_data:
            food = Food.objects.get(id=item['food'])
            MealFood.objects.create(meal=meal, food=food, quantity=item['quantity'])

        return meal