import os

INDEX_PATH="index/"

def cargar_indice():
    index={}
    for filename in os.listdir(INDEX_PATH):
        if filename.endswith(".txt"):
            word=filename[:-4]
            with open(os.path.join(INDEX_PATH,filename),"r",encoding="utf-8") as f:
                index[word]=set(line.strip() for line in f if line.strip())
    return index

def intersectar_recursivo(list_of_sets):
    if not list_of_sets: return set()
    if len(list_of_sets)==1: return list_of_sets[0]
    return list_of_sets[0].intersection(intersectar_recursivo(list_of_sets[1:]))

def buscar(q,index):
    words=q.lower().split()
    posting=[]
    for w in words:
        posting.append(index.get(w,set()))
    return intersectar_recursivo(posting)

if __name__=="__main__":
    index=cargar_indice()
    while True:
        q=input("consulta: ")
        if q=="salir": break
        print(buscar(q,index))
