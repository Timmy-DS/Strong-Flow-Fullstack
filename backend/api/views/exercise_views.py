from .base import PublicAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Exercise
from ..serializers import ExerciseSerializers
from api.services.exercise_service import update_exercise, delete_exercise, create_exercise_from_api

class ExerciseItemAPIView(PublicAPIView):
    
    def get(self, request):
        items = Exercise.objects.all()
        serializer = ExerciseSerializers(items, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
      result = create_exercise_from_api(request.data)
      return Response(result, status=status.HTTP_201_CREATED)

class ExerciseItemDetailAPIView(PublicAPIView):
    
    def get(self, request, pk):
        item = get_object_or_404(Exercise, pk=pk)
        serializer = ExerciseSerializers(item)
        return Response(serializer.data)
    

    def put(self, request, pk):
      result = update_exercise(pk, request.data)
      return Response(result)


    def delete(self, request, pk):
        delete_exercise(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)