from .base import PublicAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Exercise
from ..serializers import ExerciseSerializers
from api.services.exercise_service import create_exercise

class ExerciseItemAPIView(PublicAPIView):
    
    def get(self, request):
        items = Exercise.objects.all()
        serializer = ExerciseSerializers(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExerciseSerializers(data=request.data) 
        if serializer.is_valid():
            exercise = create_exercise(
                title=serializer.validated_data['title'],
                muscle_group=serializer.validated_data['muscle_group']
            )
            output_serializer = ExerciseSerializers(exercise)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseItemDetailAPIView(PublicAPIView):
    
    def get(self, request, pk):
        item = get_object_or_404(Exercise, pk=pk)
        serializer = ExerciseSerializers(item)
        return Response(serializer.data)
    
    
    #  # МЕТОД: Обновить (PUT /api/workout-items/1/)
    # def put(self, request, pk):
    #     item = get_object_or_404(WorkoutItem, pk=pk)
    #     serializer = WorkoutItemSerializers(item, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # МЕТОД: Удалить (DELETE /api/workout-items/1/)
    # def delete(self, request, pk):
    #     item = get_object_or_404(WorkoutItem, pk=pk)
    #     item.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)