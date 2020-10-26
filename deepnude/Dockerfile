# base image for tgbot
FROM python:3.8.6

# Set work dir
WORKDIR /deepnude/

# The enviroment variables
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .
