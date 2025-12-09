import pandas as pd
from pycarol import Carol, Staging
import os

# ================== CONFIGURE AQUI ==================
TENANT = "SEU_TENANT"
ORG = "SUA_ORG"
APP = "SEU_APP"
FILE_NAME = "airports.dat"     # agora na raiz
FILE_PATH = FILE_NAME
# ====================================================

def main():
    print("Iniciando Batch...")

    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"Arquivo {FILE_NAME} não encontrado na raiz do container.")

    print(f"Lendo arquivo {FILE_PATH}...")
    df = pd.read_csv(FILE_PATH, sep=",")   # ajuste após me dizer o separador

    print("Conectando na Carol...")
    carol = Carol(tenant=TENANT, org=ORG, app=APP)
    staging = Staging(carol)

    print("Enviando para Staging Carol...")
    staging.send_data(
        df,
        staging_name="airports_batch",
        incremental=False
    )

    print("✔ Finalizado com sucesso!")
    

if __name__ == "__main__":
    main()