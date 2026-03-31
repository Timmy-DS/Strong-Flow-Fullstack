from django.urls import path
from .views.exercise_views import ExerciseItemAPIView 


urlpatterns = [
   path('exercises/', ExerciseItemAPIView.as_view(), name='exercise-list'),
]