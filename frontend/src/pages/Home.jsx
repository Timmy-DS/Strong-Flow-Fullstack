import React, { useEffect } from 'react';
import useExerciseStore from '../store/useExerciseStore'

function Home() {
    // Достаем данные и функцию из стора
    const { exercises, getExercises } = useExerciseStore();

    useEffect(() => {
        getExercises(); // Вызываем загрузку при старте
    }, []);

    return (
        <div>
            <h1>Заметки/Упражнения</h1>
            {exercises.map((item) => (
                <div key={item.id}>{item.title || item.name}</div>
            ))}
        </div>
    );
}

export default Home;