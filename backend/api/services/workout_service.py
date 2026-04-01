from ..models import Workout
from django.shortcuts import get_object_or_404
from ..serializers import WorkoutSerializers

def create_workout(note: str) -> Workout:
    return Workout.objects.create(note=note)


def create_workout_from_api(data: dict):
    serializer = WorkoutSerializers(data=data)
    serializer.is_valid(raise_exception=True)
    workout = create_workout(**serializer.validated_data)
    output_serializer = WorkoutSerializers(workout)
    return output_serializer.data
    

def update_workout(exercise_id, data):
    exercise = get_object_or_404(Workout, pk=exercise_id)
    serializer = WorkoutSerializers(exercise, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_workout(exercise_id):
    exercise = get_object_or_404(Workout, pk=exercise_id)
    exercise.delete()
    return True