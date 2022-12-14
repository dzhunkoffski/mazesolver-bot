# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /mazesolver-bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

CMD [ "python3", "bot.py"]