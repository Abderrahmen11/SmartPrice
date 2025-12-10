# SmartPrice - Mini House Price Predictor

A simple machine learning project that predicts house prices based on three features:
- **RM**: Average number of rooms per dwelling
- **DIS**: Weighted distances to five Boston employment centres
- **LSTAT**: % lower status of the population

The project consists of a **Flask** backend (serving a Linear Regression model) and a **React + Material UI** frontend.

## 📂 Project Structure

```
SmartPrice/
├── backend/
│   ├── data.csv            # Dataset (generated or loaded)
│   ├── model.pkl           # Trained model
│   ├── train.py            # Training script
│   ├── api.py              # Flask API
│   └── requirements.txt    # Backend dependencies
└── frontend/
    ├── src/                # React source code
    ├── package.json        # Frontend dependencies
    └── ...
```

## ▶️ Run Instructions

### Backend

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python train.py
   ```
   *(This will generate `data.csv` and `model.pkl`)*
4. Start the API server:
   ```bash
   python api.py
   ```
   The API will run at `http://localhost:5000`.

### Frontend

1. Open a new terminal and navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173` (or similar).

## 🧪 Sample API Test

You can test the API directly using `curl` or Postman:

**POST** `http://localhost:5000/predict`

**Body (JSON):**
```json
{
  "rm": 6,
  "dis": 4,
  "lstat": 8
}
```

**Response:**
```json
{
  "prediction": 25.1234
}
```
