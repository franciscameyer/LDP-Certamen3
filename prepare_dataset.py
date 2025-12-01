import pandas as pd
import os
import re

CSV_PATH = "videoGames.csv"
OUTPUT_DIR = "data"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')[:40]

def main():
    df = pd.read_csv(CSV_PATH)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i, row in df.iterrows():
        name=str(row["name"])
        desc=str(row["description"])
        if desc=="nan":
            desc=""
        rank=int(row["rank"])
        filename=f"{rank:03d}_{slugify(name)}.txt"
        with open(os.path.join(OUTPUT_DIR, filename),"w",encoding="utf-8") as f:
            f.write(desc)

if __name__=="__main__":
    main()
