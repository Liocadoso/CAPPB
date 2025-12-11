FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY batch_airports.py .
COPY airports.dat .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "batch_airports.py"]