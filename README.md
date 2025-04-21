# Water Potability Predictor

A full-stack machine learning web application that predicts whether water is **potable (safe to drink)** based on physicochemical features.

Built with:

- Scikit-learn (RandomForestClassifier)
- FastAPI (API backend)
- Docker (containerized deployment)
- HTML + JavaScript (frontend)
- Hosted on Render (free tier)
---

## Acknowledgement
---
This project is a sample end-to-end machine learning workflow, including deployment, created for educational and practice purposes.

## Dataset

- **Source:** 
The dataset used in this project is available on Kaggle – Water Quality and Potability: [Kaggle – Water Quality and Potability](https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability).
Please download the data directly from Kaggle and place it in the /data folder before running the code.
- **Features:** pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity
- **Target:** Potability (1 = Safe, 0 = Not Safe)

---

## Model

- Algorithm: `RandomForestClassifier`
- Preprocessing: `StandardScaler`


---

## Live App

- **Frontend:** [https://ml-water-porability.onrender.com](https://ml-water-porability.onrender.com)
- **API Endpoint:** `https://ml-water-porability.onrender.com/predict`

---

## API Usage

**Request:**

```bash
curl -X POST https://ml-water-porability.onrender.com/predict -H "Content-Type: application/json" -d '{"ph":6.5,"Hardness":200,"Solids":20000,"Chloramines":7,"Sulfate":300,"Conductivity":400,"Organic_carbon":15,"Trihalomethanes":75,"Turbidity":4.5}'
```

**Response:**

```json
{"potability_prediction": 1}
```

---

## Frontend

- File: `src/templates/index.html`
- Built with plain HTML + JavaScript
- Hosted by FastAPI at route `/`
- Uses `fetch()` to interact with the API

---

## Dockerfile

```Dockerfile
FROM python:3.13.2

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
CMD ["uvicorn", "predictor:app", "--host", "0.0.0.0", "--port", "8080"]
```

---

## Requirements

```txt
fastapi
uvicorn
pydantic
scikit-learn
pandas
joblib
jinja2
```

---

## Author

Built by Roozbeh Ghasemi  
