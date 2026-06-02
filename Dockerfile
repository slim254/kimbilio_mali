# Multi-stage Dockerfile for Kimbilio Mali
FROM node:22-alpine AS frontend-build
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
COPY . .

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt* ./
RUN pip install --no-cache-dir -r requirements.txt || true
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
