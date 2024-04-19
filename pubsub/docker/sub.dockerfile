FROM python:3.7-alpine

WORKDIR /app

COPY ../ /app
WORKDIR /app

RUN pip install redis

CMD ["python", "-u", "sub.py"]
