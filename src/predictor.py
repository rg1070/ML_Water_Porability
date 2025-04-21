from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Allow all origins for dev/testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to specific origin later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

class WaterData(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

@app.post("/predict")
def predict(data: WaterData):
    df = pd.DataFrame([data.dict()])
    X_scaled = scaler.transform(df)
    pred = model.predict(X_scaled)[0]
    return {"potability_prediction": int(pred)}
