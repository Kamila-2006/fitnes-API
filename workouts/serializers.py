from rest_framework import serializers
from .models import Workout, WorkoutExercise


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'date', 'duration', 'exercises']

    def get_exercises(self, obj):
        workout_exercises = WorkoutExercise.objects.filter(workout=obj)

        return [
            {
                'id': workout_exercise.exercise.id,
                'name': workout_exercise.exercise.name,
                'sets': workout_exercise.sets,
                'reps': workout_exercise.reps,
                'weight': workout_exercise.weight,
            }
            for workout_exercise in workout_exercises
        ]