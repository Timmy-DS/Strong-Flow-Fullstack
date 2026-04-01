import { create } from 'zustand';
import api from "../api";

const useExerciseStore = create((set) => ({
    exercises: [], // Это ваше состояние (вместо useState)
    
    // Ваша функция в нужном вам стиле
    getExercises: () => {
        api
            .get("/api/exercises/")
            .then((res) => res.data)
            .then((data) => { 
                set({ exercises: data }); // Обновляем стор через set
                console.log(data); 
            })
            .catch((err) => alert(err));
    }
}));

export default useExerciseStore;