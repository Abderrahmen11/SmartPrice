from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os
import json

app = Flask(__name__)
CORS(app)

# Load Model and Metadata
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'model.pkl')
metadata_path = os.path.join(base_dir, 'model_metadata.json')

if not os.path.exists(model_path) or not os.path.exists(metadata_path):
    raise FileNotFoundError(f"Model or metadata not found at {model_path} / {metadata_path}. Please run train.py first.")

model = joblib.load(model_path)
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

MIN_OBSERVED_MEDV = metadata.get('min_medv', 0.0)
MAX_OBSERVED_MEDV = metadata.get('max_medv', 50.0)
VALID_RANGES = metadata.get('valid_ranges', {
    'rm': [3, 9],
    'dis': [1, 12],
    'lstat': [0, 40]
})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        try:
            rm = float(data.get('rm'))
            dis = float(data.get('dis'))
            lstat = float(data.get('lstat'))
        except (ValueError, TypeError):
             return jsonify({'error': "Invalid input type. Please provide numbers."}), 400

        # Input Validation
        if not (VALID_RANGES['rm'][0] <= rm <= VALID_RANGES['rm'][1]):
             return jsonify({'error': f"RM must be between {VALID_RANGES['rm'][0]} and {VALID_RANGES['rm'][1]}", 'validRanges': VALID_RANGES}), 400
        
        if not (VALID_RANGES['dis'][0] <= dis <= VALID_RANGES['dis'][1]):
             return jsonify({'error': f"DIS must be between {VALID_RANGES['dis'][0]} and {VALID_RANGES['dis'][1]}", 'validRanges': VALID_RANGES}), 400
             
        if not (VALID_RANGES['lstat'][0] <= lstat <= VALID_RANGES['lstat'][1]):
             return jsonify({'error': f"LSTAT must be between {VALID_RANGES['lstat'][0]} and {VALID_RANGES['lstat'][1]}", 'validRanges': VALID_RANGES}), 400
        
        # Prediction
        features = np.array([[rm, dis, lstat]])
        raw_prediction = float(model.predict(features)[0])
        
        # Clamping
        prediction = max(MIN_OBSERVED_MEDV, raw_prediction)
        
        # Unreliable Flag Logic
        # 1. If we had to clamp it (prediction != raw_prediction)
        # 2. If inputs are near edges (within 5% of range boundaries) (simplified heuristic)
        unreliable = False
        
        if prediction != raw_prediction:
            unreliable = True
        
        # Check "near edges"
        def is_near_edge(value, range_min, range_max, threshold_percent=0.05):
            r = range_max - range_min
            return value < (range_min + threshold_percent * r) or value > (range_max - threshold_percent * r)

        if (is_near_edge(rm, VALID_RANGES['rm'][0], VALID_RANGES['rm'][1]) or
            is_near_edge(dis, VALID_RANGES['dis'][0], VALID_RANGES['dis'][1]) or
            is_near_edge(lstat, VALID_RANGES['lstat'][0], VALID_RANGES['lstat'][1])):
            unreliable = True

        # Construct Response
        response = {
            "raw_prediction": round(raw_prediction, 2),
            "prediction": round(prediction, 2),
            "min_observed_MEDV": round(MIN_OBSERVED_MEDV, 2),
            "max_observed_MEDV": round(MAX_OBSERVED_MEDV, 2),
            "unreliable": unreliable
        }
        
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
