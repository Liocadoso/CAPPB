from pycarol import Carol, Staging
import pandas as pd
import os

FILE_NAME = "airports.dat"
FILE_PATH = FILE_NAME

def main():
    print("\n===== Iniciando Batch =====")

    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"Arquivo {FILE_NAME} não encontrado no container")

    print(f"Lendo arquivo {FILE_PATH}...")
    df = pd.read_csv(FILE_PATH, sep=",")
    print("Prévia do dataframe:")
    print(df.head())

    print("\nConectando na Carol...")
    carol = Carol()  # <-- SEM parâmetros!

    staging = Staging(carol)

    print("Enviando staging...")
    staging.send_data(
        df,
        staging_name="airports_batch",
        incremental=False
    )

    print("\n✔ Finalizado com sucesso no App Batch!")


if __name__ == "__main__":
    main()