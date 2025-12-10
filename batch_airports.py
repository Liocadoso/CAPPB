from pycarol import Carol, Storage, CarolDataModel
import pandas as pd
import os

FILE_NAME = "airports.dat"
DM_NAME = "airports_batch"     

def main():
    print("\n===== Batch Airports =====\n")

    if not os.path.exists(FILE_NAME):
        raise FileNotFoundError(f"❌ Arquivo {FILE_NAME} não encontrado no container\n"
                                "Verifique se está na raiz junto do Dockerfile.")

    print(f"Lendo arquivo {FILE_NAME}...")
    df = pd.read_csv(FILE_NAME, sep=",")   
    print("\n📊 Prévia:\n", df.head())

    print("\nConectando na Carol...")
    carol = Carol()
    storage = Storage(carol)
    dm = CarolDataModel(carol)

    # ------------  1) Salvar arquivo no Storage  ----------------
    output = "/tmp/storage/airports.csv"
    df.to_csv(output, index=False)

    storage.save(
        name="airports.csv",
        obj_path=output,
        content_type="text/csv"
    )
    print("\n💾 Arquivo salvo no Storage da Carol\n")

    # ------------  2) Inserir no DataModel  ---------------------
    print(f"Inserindo no DataModel '{DM_NAME}' ...")
    dm.ingest(df, model_name=DM_NAME)

    print("\n🚀 Processo finalizado com sucesso!")
    print("📍 Storage disponível na aba STORAGE do App")
    print(f"📍 Dados disponíveis no DataModel: {DM_NAME}\n")


if __name__ == "__main__":
    main()