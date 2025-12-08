from fastapi import FastAPI, HTTPException

app = FastAPI()

# Lista de arquivos disponíveis (exemplo)
FILES = [
    {"id": "f1", "name": "airports_full.csv", "url": "/files/f1/content"},
    {"id": "f2", "name": "airports_delta.csv", "url": "/files/f2/content"}
]

@app.get("/files")
def list_files():
    return FILES


@app.get("/files/{file_id}/content")
def get_file_content(file_id: str):
    if file_id == "f1":
        return {
            "content": "aeroporto_id,aeroporto_nome,iata\n1,Goroka,GKA"
        }
    if file_id == "f2":
        return {
            "content": "aeroporto_id,aeroporto_nome,iata\n2,Outro Aeroporto,XYZ"
        }

    raise HTTPException(status_code=404, detail="Arquivo não encontrado")
