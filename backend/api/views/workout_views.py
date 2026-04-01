from .base import PublicAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Workout
from ..serializers import WorkoutSerializers
from api.services.workout_service import create_workout_from_api, update_workout, delete_workout


class WorkoutAPIView(PublicAPIView):
    def get(self, request):
        items = Workout.objects.all()
        serializer = WorkoutSerializers(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        result = create_workout_from_api(request.data)
        return Response(result, status=status.HTTP_201_CREATED)
        

class WorkoutDetailAPIView(PublicAPIView):
    
    def get(self, request, pk):
        item = get_object_or_404(Workout, pk=pk)
        serializer = WorkoutSerializers(item)
        return Response(serializer.data)
    

    def put(self, request, pk):
      result = update_workout(pk, request.data)
      return Response(result)


    def delete(self, request, pk):
        delete_workout(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
