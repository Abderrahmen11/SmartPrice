import React, { useState, useEffect } from 'react';
import { TextField, Button, Box, Typography, Paper, Alert } from '@mui/material';

const PredictionForm = ({ onPredict, apiError, unreliable }) => {
    const [values, setValues] = useState({
        rm: '',
        dis: '',
        lstat: ''
    });

    const [errors, setErrors] = useState({
        rm: '',
        dis: '',
        lstat: ''
    });

    const ranges = {
        rm: { min: 3, max: 9, label: "Entre 3 et 9" },
        dis: { min: 1, max: 12, label: "Entre 1 et 12" },
        lstat: { min: 0, max: 40, label: "Entre 0 et 40" }
    };

    const validateField = (name, value) => {
        if (value === '') return '';
        const numVal = parseFloat(value);
        if (isNaN(numVal)) return "Must be a number";

        const range = ranges[name];
        if (numVal < range.min || numVal > range.max) {
            return `Value must be between ${range.min} and ${range.max}`;
        }
        return '';
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        const error = validateField(name, value);

        setValues({
            ...values,
            [name]: value
        });

        setErrors({
            ...errors,
            [name]: error
        });
    };

    const isValid = () => {
        const hasValues = values.rm !== '' && values.dis !== '' && values.lstat !== '';
        // Also check if any field has an error string
        const noErrors = !errors.rm && !errors.dis && !errors.lstat &&
            validateField('rm', values.rm) === '' &&
            validateField('dis', values.dis) === '' &&
            validateField('lstat', values.lstat) === '';

        return hasValues && noErrors;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (isValid()) {
            onPredict(values);
        }
    };

    return (
        <Paper elevation={3} sx={{ p: 4, maxWidth: 500, mx: 'auto', mt: 4 }}>
            <Typography variant="h5" gutterBottom component="div" sx={{ fontWeight: 'bold', color: '#1976d2' }}>
                Enter House Details
            </Typography>

            {apiError && <Alert severity="error" sx={{ mb: 2 }}>{apiError}</Alert>}

            {unreliable && (
                <Alert severity="warning" sx={{ mb: 2 }}>
                    ⚠ Résultat potentiellement peu fiable (valeurs extrêmes).
                </Alert>
            )}

            <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
                <TextField
                    label="Average Rooms per Dwelling (RM)"
                    name="rm"
                    type="number"
                    value={values.rm}
                    onChange={handleChange}
                    required
                    fullWidth
                    placeholder={ranges.rm.label}
                    error={!!errors.rm}
                    helperText={errors.rm || ranges.rm.label}
                    inputProps={{ step: "0.1", min: ranges.rm.min, max: ranges.rm.max }}
                />
                <TextField
                    label="Weighted Distances to Employment Centres (DIS)"
                    name="dis"
                    type="number"
                    value={values.dis}
                    onChange={handleChange}
                    required
                    fullWidth
                    placeholder={ranges.dis.label}
                    error={!!errors.dis}
                    helperText={errors.dis || ranges.dis.label}
                    inputProps={{ step: "0.1", min: ranges.dis.min, max: ranges.dis.max }}
                />
                <TextField
                    label="% Lower Status of Population (LSTAT)"
                    name="lstat"
                    type="number"
                    value={values.lstat}
                    onChange={handleChange}
                    required
                    fullWidth
                    placeholder={ranges.lstat.label}
                    error={!!errors.lstat}
                    helperText={errors.lstat || ranges.lstat.label}
                    inputProps={{ step: "0.1", min: ranges.lstat.min, max: ranges.lstat.max }}
                />
                <Button
                    variant="contained"
                    size="large"
                    type="submit"
                    sx={{ mt: 2 }}
                    disabled={!isValid()}
                >
                    Predict Price
                </Button>
            </Box>
        </Paper>
    );
};

export default PredictionForm;
