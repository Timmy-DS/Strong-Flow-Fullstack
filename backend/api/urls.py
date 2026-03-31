from django.urls import path
from .views.exercise_views import ExerciseItemAPIView, ExerciseItemDetailAPIView


urlpatterns = [
   path('exercises/', ExerciseItemAPIView.as_view(), name='exercise-list'),
   path('exercises/<int:pk>/', ExerciseItemDetailAPIView.as_view(), name='exercise-detail'),

]