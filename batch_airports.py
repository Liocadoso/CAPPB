from pycarol import Carol, BQ, Storage
import pandas as pd
import os

carol = Carol()
bq = BQ(carol)
storage = Storage(carol)

# -------- 1) Ler .dat na raiz do projeto (após COPY no Docker) --------
file_path = "/app/dataset/arquivo.dat"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

df = pd.read_csv(file_path, sep=";", encoding="utf-8")  

# -------- 2) Inserir no datamodel --------
bq.insert(df, dm_name="airport_batch")

# -------- 3) Expor resultado no Storage (opcional) --------
output_file = "/tmp/storage/resultado.csv"
df.to_csv(output_file, index=False)

storage.save(
    name="resultado.csv",
    obj_path=output_file,
    content_type="text/csv"
)

print("✔ Finalizado — Dados carregados para o DataModel e storage gerado!")