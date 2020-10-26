# base image for ym_server
FROM python:3.8.6-slim

ARG YM_BASE_DIR

# Set work dir
WORKDIR /$YM_BASE_DIR

# The enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .
