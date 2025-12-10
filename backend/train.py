import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os
import json

# Resolve paths relative to this script
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data.csv")
model_file = os.path.join(base_dir, "model.pkl")
metadata_file = os.path.join(base_dir, "model_metadata.json")

# Ensure data exists
if not os.path.exists(data_path):
    print(f"Generating {data_path}...")
    # Synthetic data generation if file doesn't exist
    np.random.seed(42)
    n_samples = 500
    rm = np.random.normal(6, 0.7, n_samples)
    dis = np.random.exponential(4, n_samples) + 1
    lstat = np.random.uniform(2, 35, n_samples)
    
    # MEDV relationship
    medv = 10 + 5 * rm - 0.5 * dis - 0.5 * lstat + np.random.normal(0, 3, n_samples)
    # Ensure MEDV is non-negative for training data quality
    medv = np.maximum(0, medv)
    
    df = pd.DataFrame({
        'RM': rm,
        'DIS': dis,
        'LSTAT': lstat,
        'MEDV': medv
    })
    df.to_csv(data_path, index=False)
    print(f"Saved {data_path}")
else:
    print(f"Loading {data_path}")
    df = pd.read_csv(data_path)

# Select features and target
X = df[['RM', 'DIS', 'LSTAT']]
y = df['MEDV']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model (RandomForestRegressor)
print("Training RandomForestRegressor...")
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Model Trained.")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")

# Save model
joblib.dump(model, model_file)
print(f"Model saved to {model_file}")

# Calculate and save metadata
metadata = {
    "min_medv": float(y.min()),
    "max_medv": float(y.max()),
    "valid_ranges": {
        "rm": [3, 9],
        "dis": [1, 12],
        "lstat": [0, 40]
    }
}

with open(metadata_file, 'w') as f:
    json.dump(metadata, f, indent=4)
print(f"Metadata saved to {metadata_file}")
