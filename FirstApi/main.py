from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

# 1. Simple ML Logic (The "Brain")
# In C, you'd manage these arrays manually. In Python/NumPy, they are objects.
# Data: [Sq Footage, Number of Rooms]
X = np.array([[600, 1], [800, 2], [1200, 3], [1500, 4], [2000, 5]])
# Prices: $ Price
y = np.array([150000, 200000, 300000, 375000, 500000])

model = LinearRegression()
model.fit(X, y)

# 2. Data Validation (The "Guardrail")
class HouseFeatures(BaseModel):
    sq_ft: float
    rooms: int

# 3. The API Endpoint
@app.post("/predict")
async def predict_price(features: HouseFeatures):
    input_data = np.array([[features.sq_ft, features.rooms]])
    prediction = model.predict(input_data)[0]

    return {
        "input": features,
        "estimated_price": round(prediction, 2),
        "currency": "USD"
    }

@app.get("/")
def home():
    return {"message": "AI Predictor API is Live"}