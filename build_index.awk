#!/usr/bin/awk -f
BEGIN{
    stop="stopwords.txt"
    while((getline w<stop)>0){ sw[w]=1 }
}
{
    gsub(/[^a-zA-Z0-9]/," ")
    for(i=1;i<=NF;i++){
        w=tolower($i)
        if(!(w in sw) && length(w)>0){
            print FILENAME >> ("index/" w ".txt")
        }
    }
}
