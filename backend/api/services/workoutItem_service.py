from ..models import WorkoutItem
from django.shortcuts import get_object_or_404
from ..serializers import WorkoutItemSerializers


def create_workout_item(workout: str, exercise:str, sets_data:str) -> WorkoutItem:
    return WorkoutItem.objects.create(
        workout=workout, 
        exercise=exercise,
        sets_data=sets_data  
        )


def create_workout_item_from_api(data: dict):
    serializer = WorkoutItemSerializers(data=data)
    serializer.is_valid(raise_exception=True)
    workout = create_workout_item(**serializer.validated_data)
    output_serializer = WorkoutItemSerializers(workout)
    return output_serializer.data
    

def update_workout_item(exercise_id, data):
    exercise = get_object_or_404(WorkoutItem, pk=exercise_id)
    serializer = WorkoutItemSerializers(exercise, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_workout_item(exercise_id):
    exercise = get_object_or_404(WorkoutItem, pk=exercise_id)
    exercise.delete()
    return True