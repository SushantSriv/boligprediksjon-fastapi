
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import numpy as np
import pandas as pd
import joblib
import os
import joblib
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👇 Legg til dette før du definerer endepunkter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # eller sett eksakt URL til React-app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_URL = "https://drive.google.com/uc?export=download&id=1HN502_G3HIxRmquFAvjGyCEj4R1Inn5X"

# Last ned modellen hvis den ikke finnes
if not os.path.exists("model.pkl"):
    print("📥 Laster ned model.pkl fra Google Drive...")
    r = requests.get(MODEL_URL)
    with open("model.pkl", "wb") as f:
        f.write(r.content)

# Last inn modellen
model = joblib.load("model.pkl")

# 📥 Input-modell
class PredictionInput(BaseModel):
    year: int
    month_num: int
    type_of_employment: str



# ✨ One-hot encoding mapping
employment_types = [
    "05 Detached houses of wood total, materials",
    "06 Stone, clay and cement work, total",
    "07 Stone, clay and cement work, materials",
    "08 Wood, site preparation, total",
    "09 Wood, site preparation, materials",
    "10 Wood, other building work, total",
    "11 Wood, other building work, materials",
    "12 Carpentry, total",
    "13 Carpentry, materials",
    "14 Painting, paperhanging and floor coating, total",
    "15 Painting, paperhanging and floor coating, materials",
    "16 Plumbing, total",
    "17 Plumbing, materials",
    "18 Electrical installation work, total",
    "19 Electrical installation work, materials"
]

@app.post("/predict")
def predict(data: PredictionInput):
    # Lag tom feature-vektor
    row = {}
    for e in employment_types:
        row["type of employment_{}".format(e)] = 0

    # Sett den riktige kolonnen til 1
    row["type of employment_{}".format(data.type_of_employment)] = 1

    # Legg til år og måned
    row["year"] = data.year
    row["month_num"] = data.month_num

    # Konverter til DataFrame
    df = pd.DataFrame([row])

    print("Input row:", row)
    print("DataFrame for prediksjon:\n", df)

    print("Model features:", model.feature_names_in_)

    # Reorganiser kolonnene i riktig rekkefølge
    df = df[model.feature_names_in_]
    # Prediksjon
    pred = model.predict(df)[0]
    return {"predicted_index": round(pred, 2)}
