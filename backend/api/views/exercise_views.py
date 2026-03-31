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
