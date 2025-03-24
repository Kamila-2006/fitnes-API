from rest_framework import serializers
from .models import Workout, WorkoutExercise


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'date', 'duration', 'exercises']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        workout_exercises = WorkoutExercise.objects.filter(workout=instance)

        representation['exercises'] = [
            {
                'id': workout_exercise.exercise.id,
                'name': workout_exercise.exercise.name,
                'sets': workout_exercise.sets,
                'reps': workout_exercise.reps,
                'weight': workout_exercise.weight,
            }
            for workout_exercise in workout_exercises
        ]
        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        workout = Workout.objects.create(**validated_data)

        return workout