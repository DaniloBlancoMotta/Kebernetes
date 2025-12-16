# Churn Prediction Service (Lesson 10)

This repository contains a Machine Learning service for predicting customer churn, deployed using Docker and Kubernetes.

## Structure

*   `predict.py`: Flask application for serving predictions.
*   `model_C=10.bin`: Pre-trained Logistic Regression model.
*   `Dockerfile`: Configuration for building the Docker image.
*   `kubernetes/`: manifest files for Kubernetes deployment.
    *   `deployment.yaml`: Defines the Deployment resource.
    *   `service.yaml`: Defines the Service resource.

## Local Development

1.  **Install dependencies**:
    ```bash
    pipenv install
    ```

2.  **Run locally**:
    ```bash
    pipenv shell
    python predict.py
    ```

## Docker

Build the image:
```bash
docker build -t zoomcamp-model:v1 .
```

Run the container:
```bash
docker run -it --rm -p 9696:9696 zoomcamp-model:v1
```

## Kubernetes (Kind)

Load image:
```bash
kind load docker-image zoomcamp-model:v1
```

Apply manifests:
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```
