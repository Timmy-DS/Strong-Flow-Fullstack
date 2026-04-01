from .base import PublicAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import WorkoutItem
from ..serializers import WorkoutItemSerializers
from api.services.workoutItem_service import create_workout_item_from_api, update_workout_item, delete_workout_item


class WorkoutItemAPIView(PublicAPIView):
    def get(self, request):
        items = WorkoutItem.objects.all()
        serializer = WorkoutItemSerializers(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        result = create_workout_item_from_api(request.data)
        return Response(result, status=status.HTTP_201_CREATED)
        

class WorkoutItemDetailAPIView(PublicAPIView):
    
    def get(self, request, pk):
        item = get_object_or_404(WorkoutItem, pk=pk)
        serializer = WorkoutItemSerializers(item)
        return Response(serializer.data)
    

    def put(self, request, pk):
      result = update_workout_item(pk, request.data)
      return Response(result)


    def delete(self, request, pk):
        delete_workout_item(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
