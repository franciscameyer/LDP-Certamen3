import os

INDEX_PATH="index/"

def load_index():
    index={}
    for filename in os.listdir(INDEX_PATH):
        if filename.endswith(".txt"):
            word=filename[:-4]
            with open(os.path.join(INDEX_PATH,filename),"r",encoding="utf-8") as f:
                index[word]=set(line.strip() for line in f if line.strip())
    return index

def intersect_recursive(list_of_sets):
    if not list_of_sets: return set()
    if len(list_of_sets)==1: return list_of_sets[0]
    return list_of_sets[0].intersection(intersect_recursive(list_of_sets[1:]))

def search(q,index):
    words=q.lower().split()
    posting=[]
    for w in words:
        posting.append(index.get(w,set()))
    return intersect_recursive(posting)

if __name__=="__main__":
    index=load_index()
    while True:
        q=input("consulta: ")
        if q=="salir": break
        print(search(q,index))
