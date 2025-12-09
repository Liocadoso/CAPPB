# Usa uma imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY batch_airports.py .

# Copia o arquivo airports.dat para dentro da imagem
COPY airports.dat .

# Comando padrão para rodar o processo
CMD ["python", "batch_airports.py"]
