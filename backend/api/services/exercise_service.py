from ..models import Exercise
from django.shortcuts import get_object_or_404
from ..serializers import ExerciseSerializers


def create_exercise(title: str, muscle_group: str) -> Exercise:
    return Exercise.objects.create(
        title=title, 
        muscle_group=muscle_group)


def create_exercise_from_api(data: dict):
    serializer = ExerciseSerializers(data=data)
    serializer.is_valid(raise_exception=True)
    exercise = create_exercise(**serializer.validated_data)
    output_serializer = ExerciseSerializers(exercise)
    return output_serializer.data
  

def update_exercise(exercise_id, data):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    serializer = ExerciseSerializers(exercise, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_exercise(exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    exercise.delete()
    return True