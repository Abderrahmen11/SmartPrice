import React from 'react';
import { Container, Typography, Paper, Box } from '@mui/material';

const About = () => {
    return (
        <Container maxWidth="md">
            <Paper elevation={3} sx={{ p: 4, mt: 8 }}>
                <Typography variant="h4" gutterBottom sx={{ fontWeight: 'bold' }}>
                    About SmartPrice
                </Typography>
                <Typography variant="body1" paragraph>
                    SmartPrice is a minimal machine learning project designed to demonstrate a full-stack ML application.
                </Typography>
                <Typography variant="h6" gutterBottom sx={{ mt: 2 }}>
                    How it works:
                </Typography>
                <Typography variant="body1" component="div">
                    <ul>
                        <li><strong>Backend:</strong> Flask API serving a Linear Regression model trained on housing data.</li>
                        <li><strong>Frontend:</strong> React + Material UI interface for user interaction.</li>
                        <li><strong>Inputs:</strong>
                            <ul>
                                <li>RM: Average number of rooms per dwelling</li>
                                <li>DIS: Weighted distances to employment centres</li>
                                <li>LSTAT: % lower status of the population</li>
                            </ul>
                        </li>
                    </ul>
                </Typography>
            </Paper>
        </Container>
    );
};

export default About;
