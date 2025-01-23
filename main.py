from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from model import train_model, make_prediction

# Initialize FastAPI app
app = FastAPI()

# File paths
DATASET_PATH = "uploaded_data.csv"
MODEL_PATH = "model.pkl"

# Endpoint 1: Upload CSV File
@app.post("/upload")
async def upload_file(file: UploadFile):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")
    
    # Read and save the file
    try:
        df = pd.read_csv(file.file)
        df.to_csv(DATASET_PATH, index=False)
        return {"message": "File uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")

# Endpoint 2: Train the Model
@app.post("/train")
async def train():
    try:
        # Load dataset
        df = pd.read_csv(DATASET_PATH)
        metrics = train_model(df, MODEL_PATH)
        return {"message": "Model trained successfully.", "metrics": metrics}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Dataset not found. Please upload a dataset first.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to train model: {str(e)}")

# Request body schema for prediction
class PredictionInput(BaseModel):
    Temperature: float
    Run_Time: float

# Endpoint 3: Make Predictions
@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        # Make a prediction
        prediction, confidence = make_prediction(MODEL_PATH, input_data.dict())
        return {"Downtime": "Yes" if prediction else "No", "Confidence": confidence}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Model not found. Please train a model first.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to make prediction: {str(e)}")
