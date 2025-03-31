from rest_framework import serializers
from .models import Workout, WorkoutExercise
from exercises.models import Exercise


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = serializers.ListSerializer(child=serializers.DictField(), write_only=True)

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
        exercises_data = validated_data.pop('exercises', [])
        workout = Workout.objects.create(user=user, **validated_data)

        for item in exercises_data:
            exercise = Exercise.objects.get(id=item['exercise'])
            WorkoutExercise.objects.create(
                workout=workout,
                exercise=exercise,
                sets=item['sets'],
                reps=item['reps'],
                weight=item['weight']
            )

        return workout

    def update(self, instance, validated_data):
        exercises_data = validated_data.pop('exercises', [])

        instance.date = validated_data.get('date', instance.date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()

        if exercises_data:
            instance.workout_exercises.all().delete()

            for item in exercises_data:
                exercise = Exercise.objects.get(id=item['exercise'])
                WorkoutExercise.objects.create(
                    workout=instance,
                    exercise=exercise,
                    sets=item['sets'],
                    reps=item['reps'],
                    weight=item['weight']
                )

        return instance