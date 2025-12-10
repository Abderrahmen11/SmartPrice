import axios from 'axios';

const API_URL = 'http://localhost:5000/predict';

export const getPrediction = async (data) => {
    try {
        const response = await axios.post(API_URL, data);
        return response.data;
    } catch (error) {
        // Propagate the specific error message from the backend if available
        if (error.response && error.response.data && error.response.data.error) {
             throw new Error(error.response.data.error);
        }
        console.error("Error fetching prediction:", error);
        throw error;
    }
};
