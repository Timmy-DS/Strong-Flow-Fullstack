from rest_framework import serializers
from .models import Exercise, Workout, WorkoutItem

class ExerciseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "title", "muscle_group"]
        
class WorkoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "created_at", "note"]
    
class WorkoutItemSerializers(serializers.ModelSerializer):
    sets_data = serializers.JSONField()
    muscle_group = serializers.ReadOnlyField(source="exercise.muscle_group")
    exercise_title = serializers.ReadOnlyField(source='exercise.title')
    class Meta:
        model = WorkoutItem
        fields = ["id", "workout", "exercise", "sets_data", "muscle_group", "exercise_title"]