import sys, os

stopwords=set(line.strip() for line in open("stopwords.txt",encoding="utf-8") if line.strip())

#Elimina stopwords de forma recursiva y acumula las removidas
def eliminar_stopwords_recursivo(words, removed=None):
    if removed is None: removed=[]
    if not words: return [], removed
    first,*rest=words
    if first.lower() in stopwords:
        removed.append(first)
        return eliminar_stopwords_recursivo(rest, removed)
    cleaned_rest, removed = eliminar_stopwords_recursivo(rest, removed)
    return [first]+cleaned_rest, removed

#Procesa un archivo, eliminando stopwords de cada linea
def procesar_archivo(input_path, output_path):
    with open(input_path,"r",encoding="utf-8") as f:
        lines=f.readlines()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path,"w",encoding="utf-8") as out:
        for line in lines:
            words = line.strip().split()
            cleaned, removed = eliminar_stopwords_recursivo(words)
            if removed:
                print(f"Removidas en línea: {', '.join(removed)}")
            out.write(" ".join(cleaned) + "\n")


if __name__=="__main__":
    procesar_archivo(sys.argv[1], sys.argv[2])
