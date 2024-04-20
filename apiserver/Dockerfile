FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--port", "80", "--host", "0.0.0.0"]
