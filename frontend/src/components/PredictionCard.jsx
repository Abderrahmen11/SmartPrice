import React from 'react';
import { Card, CardContent, Typography, Box } from '@mui/material';

const PredictionCard = ({ prediction }) => {
    if (prediction === null) return null;

    return (
        <Card sx={{ maxWidth: 500, mx: 'auto', mt: 4, bgcolor: '#e3f2fd' }}>
            <CardContent>
                <Typography variant="h6" color="text.secondary" gutterBottom>
                    Estimated House Price
                </Typography>
                <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', py: 2 }}>
                    <Typography variant="h3" component="div" sx={{ fontWeight: 'bold', color: '#1565c0' }}>
                        ${prediction.toFixed(2)}k
                    </Typography>
                </Box>
                <Typography variant="body2" color="text.secondary" align="center">
                    Based on the provided features.
                </Typography>
            </CardContent>
        </Card>
    );
};

export default PredictionCard;
