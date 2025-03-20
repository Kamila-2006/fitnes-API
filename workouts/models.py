from django.db import models
from users.models import User
from exercises.models import Exercise


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
    duration = models.DurationField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='workout_exercises')
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)