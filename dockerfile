FROM python:3.13.2

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD ["uvicorn", "predictor:app", "--host", "0.0.0.0", "--port", "8080"]
