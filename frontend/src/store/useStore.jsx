import { create } from 'zustand'
import axios from 'axios'


const useWorkoutStore = create((set) => ({
    workoutItems: [],
    isLoading: false,
    error: null,

    fetchWorkoutItems: async () => {
        set({ isLoading: true, error: null});
        try {
            const responce = await axios.get('http://127.0.0.1')
            set({workoutItems: responce.data, isLoading: false});

        } catch (err) {
            set({error: err.message, isLoading: false})
        }
    },
}))



export default useWorkoutStore