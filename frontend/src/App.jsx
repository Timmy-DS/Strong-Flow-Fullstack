import { useState, useEffect } from 'react';
import axios from 'axios';
import { create } from 'zustand';
import Home from "./pages/Home"

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
   return (
    <Home />
   )
}

export default App;
