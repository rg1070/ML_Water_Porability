# 💧 Water Potability Predictor (End-to-End MLOps)

This project is a complete, real-time MLOps pipeline that predicts whether water is potable (safe to drink) using sensor data.

It includes:
- 🧠 Model training with RandomForest (Scikit-learn)
- 🚀 REST API with FastAPI
- 🐳 Dockerized deployment on Render.com
- 🌐 HTML + JavaScript frontend interface
- 🧪 Real-time prediction and testing

---

## 📊 Dataset

- Source: [Kaggle Water Quality Dataset](https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability)
- Features: pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity
- Target: Potability (1 = Safe, 0 = Unsafe)

---

## 🧪 Model Info

- Classifier: `RandomForestClassifier`
- Preprocessing: `StandardScaler`
- Accuracy: ~ (check notebook)
- Trained in: `notebooks/model_training.ipynb`

---

## 🛠️ API Usage (FastAPI)

### Endpoint: `POST /predict`

Example:

```json
{
  "ph": 6.5,
  "Hardness": 200,
  "Solids": 20000,
  "Chloramines": 7,
  "Sulfate": 300,
  "Conductivity": 400,
  "Organic_carbon": 15,
  "Trihalomethanes": 75,
  "Turbidity": 4.5
}
