# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN mkdir -p /app/download

COPY app.py /app/app.py

RUN pip3 install flask

RUN pip3 install yt-dlp

RUN apt -y update 

RUN apt -y install ffmpeg

EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
