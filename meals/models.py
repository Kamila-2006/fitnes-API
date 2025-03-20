from django.db import models
from users.models import User
from foods.models import Food


class Meal(models.Model):

    MEAL_TYPE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField()
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE_CHOICES)
    foods = models.ManyToManyField(Food, through='MealFood')

    def __str__(self):
        return f'{self.meal_type} for {self.user}'

class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_food')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='meal_food')
    quantity = models.DecimalField(max_digits=3, decimal_places=1)