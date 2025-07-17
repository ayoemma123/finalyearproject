FROM python:3.10-slim

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt --verbose

COPY . .

EXPOSE 8000 

CMD gunicorn finalproject.wsgi:application --bind 0.0.0.0:8000

