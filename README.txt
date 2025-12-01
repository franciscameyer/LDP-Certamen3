Certamen 3 - Motor de búsqueda con índice invertido
===================================================

Integrantes
-----------
- Francisca Meyer
- Lukas Scheel

Resumen
-------
Motor de búsqueda en línea de comandos que construye un índice invertido a partir del dataset `videoGames.csv` (Kaggle). El flujo completo:

1) Convertir el CSV en un `.txt` por videojuego.  
2) Eliminar *stopwords* con una función recursiva en Python.  
3) Crear un archivo de postings por palabra con AWK.  
4) Atender consultas multi-palabra en Python intersectando recursivamente las listas de documentos.

Requisitos
----------
- Python 3 y `pip` (se usa `pandas`).
- AWK (el que incluye Git Bash funciona).
- `make` (también viene con Git Bash en Windows).

Instalación rápida
------------------
- Instala dependencias de Python: `python -m pip install pandas`
- En Windows usa Git Bash para que `make` y `awk` estén disponibles en PATH.

Uso recomendado con make
------------------------
```bash
make prepare      # Genera data/*.txt desde videoGames.csv
make clean_data   # Limpia stopwords recursivamente -> data_clean/
make index        # Construye el índice invertido en index/
make run          # Inicia el buscador interactivo (escribe "salir" para terminar)
# make clean      # (opcional) elimina data_clean/ e index/
```

Ejecución manual (sin make)
---------------------------
```bash
python preparar_dataset.py
mkdir -p data_clean
for f in data/*.txt; do python eliminar_stopwords.py "$f" "data_clean/$(basename "$f")"; done
mkdir -p index
awk -f build_index.awk data_clean/*.txt
python motor_busqueda.py
```

Formato de las consultas
------------------------
- La búsqueda es por intersección (AND): solo retorna documentos que contienen **todas** las palabras.
- Las palabras se normalizan a minúsculas y se ignoran stopwords.
- En la sesión interactiva usa `salir` para cerrar.
- La salida muestra el conjunto de archivos `data_clean/<rank>_<slug>.txt` donde aparece cada término.

Estructura esperada
-------------------
```
videoGames.csv
data/             # .txt originales (1 por juego)
data_clean/       # .txt sin stopwords
index/            # <palabra>.txt con la lista de documentos donde aparece
build_index.awk
eliminar_stopwords.py
motor_busqueda.py
preparar_dataset.py
stopwords.txt
Makefile
```

Archivos y decisiones clave
---------------------------
- `preparar_dataset.py`: usa `pandas` para leer el CSV y crear un `.txt` por juego con un nombre limpio (`rank_slug`).
- `eliminar_stopwords.py`: función recursiva `eliminar_stopwords_recursivo` que además imprime en consola las stopwords removidas por línea.
- `build_index.awk`: genera un archivo por palabra en `index/` con los documentos donde aparece, omitiendo stopwords.
- `motor_busqueda.py`: carga todos los postings en memoria y resuelve la consulta intersectando las listas de forma recursiva.
- `Makefile`: automatiza todo el pipeline (`prepare`, `clean_data`, `index`, `run`, `clean`).

Problemas comunes
-----------------
- `awk` o `make` no encontrados: abre Git Bash o instala una distribución Unix-like para Windows.
- `ModuleNotFoundError: pandas`: instala con `python -m pip install pandas`.
- Texto extraño en consola: asegúrate de guardar los `.py` y `.txt` en UTF-8 y ejecutar en una terminal que soporte ese encoding.

Enlaces (Links)
-----------------
- CSV: https://www.kaggle.com/datasets/kaavyamahajan/video-games-plots
- Repositorio github: https://github.com/franciscameyer/LDP-Certamen3