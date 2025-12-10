import React, { useState } from 'react';
import { Container, Typography, Box } from '@mui/material';
import PredictionForm from '../components/PredictionForm';
import PredictionCard from '../components/PredictionCard';
import { getPrediction } from '../api/predictionService';

const Home = () => {
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);
    const [unreliable, setUnreliable] = useState(false);

    const handlePredict = async (data) => {
        try {
            setError(null);
            setUnreliable(false);
            const result = await getPrediction(data);
            setPrediction(result.prediction);
            setUnreliable(result.unreliable);
        } catch (err) {
            // Error is already extracted in service if it's an API error
            setError(err.message || "Failed to get prediction. Please try again.");
            console.error(err);
        }
    };

    return (
        <Container maxWidth="md">
            <Box sx={{ my: 4, textAlign: 'center' }}>
                <Typography variant="h2" component="h1" gutterBottom sx={{ fontWeight: 'bold', color: '#333' }}>
                    SmartPrice
                </Typography>
                <Typography variant="h5" color="text.secondary" paragraph>
                    Mini House Price Predictor
                </Typography>
            </Box>

            <PredictionForm onPredict={handlePredict} apiError={error} unreliable={unreliable} />
            <PredictionCard prediction={prediction} />
        </Container>
    );
};

export default Home;
