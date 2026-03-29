from django.contrib import admin
from .models import Exercise, Workout, WorkoutItem, User

admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutItem)