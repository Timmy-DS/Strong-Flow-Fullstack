from django.urls import path
from .views.exercise_views import ExerciseItemAPIView, ExerciseItemDetailAPIView
from .views.workout_views import WorkoutAPIView, WorkoutDetailAPIView
from .views.workoutItem_views import WorkoutItemAPIView, WorkoutItemDetailAPIView


urlpatterns = [
   path('exercises/', ExerciseItemAPIView.as_view(), name='exercise-list'),
   path('exercises/<int:pk>/', ExerciseItemDetailAPIView.as_view(), name='exercise-detail'),
   
   path('workouts/', WorkoutAPIView.as_view(), name='workout-list'),
   path('workouts/<int:pk>/', WorkoutDetailAPIView.as_view(), name='workouts-detail'),
   
   path('workoutItems/', WorkoutItemAPIView.as_view(), name='workout-list-items'),
   path('workoutItems/<int:pk>/', WorkoutItemDetailAPIView.as_view(), name='workouts-list-items'),
   
]