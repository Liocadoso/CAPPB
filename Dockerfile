FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto (incluindo .dat e .py)
COPY . .

# Rodar o script Python ao iniciar o batch
CMD ["python", "batch_airports.py"]