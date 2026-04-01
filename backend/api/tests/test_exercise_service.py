import pytest
from django.http import Http404
from api.models import Exercise
from api.services.exercise_service import create_exercise, create_exercise_from_api, delete_exercise, update_exercise

@pytest.mark.django_db
class TestExerciseService:

    def test_create_exercise_success(self):
        exercise = create_exercise(title="Приседания", muscle_group="Ноги")
        assert exercise.id is not None
        assert exercise.title == "Приседания"
        assert Exercise.objects.count() == 1

    def test_create_exercise_from_api_success(self):
        data = {"title": "Жим лежа", "muscle_group": "Грудь"}
        result = create_exercise_from_api(data)
        assert result["title"] == "Жим лежа"
        assert Exercise.objects.filter(title="Жим лежа").exists()
        
    def test_update_exercise_sucess(self):
        exercise = create_exercise(title="Становая тяга", muscle_group="Спина")
        update_data = {
            "title": "Новая тяга",
            "muscle_group": "Ноги"
        }
        result = update_exercise(exercise.id, update_data)
        assert result["title"] == "Новая тяга"
        assert result["muscle_group"] == "Ноги"
        exercise.refresh_from_db()  # Обновляем данные объекта из БД
        assert exercise.title == "Новая тяга"
        assert exercise.muscle_group == "Ноги"
        

    def test_delete_exercise_success(self):
        ex = create_exercise(title="Тяга", muscle_group="Спина")
        result = delete_exercise(ex.id)
        assert result is True
        assert Exercise.objects.count() == 0

    def test_delete_exercise_not_found(self):
        with pytest.raises(Http404):
            delete_exercise(999)
