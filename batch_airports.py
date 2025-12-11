import pandas as pd
import os
from pycarol import Carol, Staging

FILE_PATH = "/app/airports.dat"
STAGING_NAME = "airportbatch"
STEP_SIZE = 5000

# Coloque o ID real do conector aqui:
CONNECTOR_ID = "6b611cb89896467d8f0c896daf19e390"

carol = Carol()
staging = Staging(carol)

print(f"Lendo arquivo: {FILE_PATH}")

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(f"Arquivo não encontrado no container: {FILE_PATH}")

df = pd.read_csv(FILE_PATH, delimiter=",", encoding="utf-8", dtype=str)
print(f"Arquivo carregado com {len(df)} registros.")

records = df.to_dict(orient="records")

print(f"Enviando {len(records)} registros à staging '{STAGING_NAME}'...")

staging.send_data(
    staging_name=STAGING_NAME,
    data=records,
    connector_id=CONNECTOR_ID,
    step_size=STEP_SIZE,
    print_stats=True
)

print("✔ Ingestão concluída com sucesso!")