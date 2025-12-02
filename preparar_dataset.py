import pandas as pd
import os
import re

CSV_PATH = "videoGames.csv"
OUTPUT_DIR = "data"

#Genera un identificador corto y limpio para nombres de archivo.
def generar_slug(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9]+", "_", texto)
    return texto.strip("_")[:40]

#Recorre el CSV y crea archivos .txt con las descripciones de cada juego.
def principal():
    df = pd.read_csv(CSV_PATH)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i, row in df.iterrows():
        name=str(row["name"])
        desc=str(row["description"])
        if desc=="nan":
            desc=""
        rank=int(row["rank"])
        filename=f"{rank:03d}_{generar_slug(name)}.txt"
        with open(os.path.join(OUTPUT_DIR, filename),"w",encoding="utf-8") as f:
            f.write(desc)

if __name__=="__main__":
    principal()
