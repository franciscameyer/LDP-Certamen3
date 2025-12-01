import sys, os

stopwords=set(line.strip() for line in open("stopwords.txt",encoding="utf-8") if line.strip())

def remove_stopwords_recursive(words, removed=None):
    if removed is None: removed=[]
    if not words: return [], removed
    first,*rest=words
    if first.lower() in stopwords:
        removed.append(first)
        return remove_stopwords_recursive(rest, removed)
    cleaned_rest, removed = remove_stopwords_recursive(rest, removed)
    return [first]+cleaned_rest, removed

def process_file(input_path, output_path):
    with open(input_path,"r",encoding="utf-8") as f:
        lines=f.readlines()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path,"w",encoding="utf-8") as out:
        for line in lines:
            words=line.strip().split()
            cleaned, removed=remove_stopwords_recursive(words)
            out.write(" ".join(cleaned)+"\n")

if __name__=="__main__":
    process_file(sys.argv[1], sys.argv[2])
