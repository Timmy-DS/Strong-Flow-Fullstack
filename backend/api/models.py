from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    current_weight = models.FloatField(blank=True, null=True) 

    def __str__(self):
        return self.username
    
    def get_weight(self):
        return self.current_weight  

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    
class Workout(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"Тренировка {self.created_at.strftime('%d.%m.%Y')}"

class WorkoutItem(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="items")
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    sets_data = models.JSONField(default=list)
    
    def __str__(self):
         return f"{self.exercise.title} в {self.workout}"