from ..models import Exercise

def create_exercise(title: str, muscle_group: str) -> Exercise:
    exercise = Exercise.objects.create(
        title = title,
        muscle_group = muscle_group
    )
    return exercise