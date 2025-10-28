# Churn Prediction Service

Serviço de predição de churn de clientes usando Machine Learning.

## Requisitos

- Python 3.8+
- Docker
- Pipenv

## Instalação Local

```bash
pipenv install
pipenv shell
python predict.py
```

## Docker

### Build
```bash
docker build -t churn-prediction .
```

### Run
```bash
docker run -p 9696:9696 churn-prediction
```

## Teste

```bash
python predict-test.py
```

## API

**Endpoint:** `POST /predict`

**Exemplo de request:**
```json
{
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "yes",
  "dependents": "no",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 1,
  "monthlycharges": 29.85,
  "totalcharges": 29.85
}
```

**Response:**
```json
{
  "churn": true,
  "churn_probability": 0.615
}
```
