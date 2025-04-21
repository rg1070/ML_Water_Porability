import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
    scaled = scaler.transform(df)
    prediction = model.predict(scaled)[0]
    return {"potability_prediction": int(prediction)}
