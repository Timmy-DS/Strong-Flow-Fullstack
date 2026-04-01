import { useState, useEffect } from 'react';
import axios from 'axios';
import { create } from 'zustand';

// 1. Создаем стор прямо здесь (обычно выносят в отдельный файл, но для теста можно так)
const useWorkoutStore = create((set) => ({
    workoutItems: [],
    fetchItems: async () => {
        try {
            // Замени URL на свой актуальный эндпоинт
            const response = await axios.get('http://127.0.0.1:8000/api/workoutItems/');
            set({ workoutItems: response.data });
        } catch (error) {
            console.error("Ошибка при загрузке:", error);
        }
    }
}));

function App() {
    // 2. Достаем данные и функцию из стора
    const { workoutItems, fetchItems } = useWorkoutStore();

    // 3. Загружаем данные при старте приложения
    useEffect(() => {
        fetchItems();
    }, []);

    return (
        <div style={{ padding: '20px' }}>
            <h1>Список тренировок</h1>
            
            {workoutItems.length === 0 && <p>Данных пока нет или загрузка...</p>}

            {workoutItems.map((item) => (
                <div key={item.id} style={{ 
                    border: '1px solid #ddd', 
                    marginBottom: '10px', 
                    padding: '10px',
                    borderRadius: '8px' 
                }}>
                    <strong>Упражнение:</strong> {item.exercise_title} <br />
                    <strong>Группа мышц:</strong> {item.muscle_group} <br />
                   <strong>Подходы:</strong> {item.sets_data.reps} повторений, {item.sets_data.weight} кг
                </div>
            ))}
        </div>
    );
}

export default App;
