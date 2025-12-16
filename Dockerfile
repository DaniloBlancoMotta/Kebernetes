FROM python:3.9-slim

# Install pipenv
RUN pip install pipenv

WORKDIR /app

# Copy Pipfiles
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install dependencies (system-wide since it's a container)
# We use --system to install into system python, avoiding virtualenv creation inside docker
# We remove --deploy to avoid hash mismatch errors during development/generated lock files
RUN pipenv install --system

# Copy application code
COPY ["predict.py", "model_C=10.bin", "./"]

# Expose port
EXPOSE 9696

# Use Gunicorn as production server
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]
