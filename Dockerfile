## Parent Image
FROM python:3.10-slim

# Essential Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/* 

## Copying your all contents from local directory to app (docker)
COPY . .

## Run setup.py
RUN pip install --no-cache-dir -e .

## Used PORTS
# Frontend
EXPOSE 8501
# Backend  
EXPOSE 9999

CMD ["python", "app/main.py"]
