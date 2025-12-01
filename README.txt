Certamen 3 – Índice Invertido
=============================

INTEGRANTES
-----------
- Francisca Meyer
- Lukas Scheel

DESCRIPCIÓN GENERAL
-------------------
Este proyecto implementa un **motor de búsqueda** basado en un **ÍNDICE INVERTIDO** a partir de un dataset de videojuegos
(obtenido desde Kaggle: https://www.kaggle.com/datasets/kaavyamahajan/video-games-plots). La idea es:

1. Convertir el CSV en múltiples archivos `.txt` (un documento por videojuego).
2. Eliminar las *stopwords* usando **recursividad** en Python.
3. Construir un índice invertido usando **AWK**, generando un archivo por palabra.
4. Cargar el índice en memoria y procesar consultas de búsqueda en Python, usando **intersección recursiva** de listas de posteo.



REPOSITORIO GIT
---------------
Repositorio del proyecto (Git):

    https://github.com/franciscameyer/LDP-Certamen3



ESTRUCTURA DEL PROYECTO
------------------------
Archivos principales:

- `preparar_dataset.py`  
  Convierte el archivo `videoGames.csv` en múltiples documentos `.txt` dentro de la carpeta `data/`.
  Cada archivo contiene la descripción del videojuego. :contentReference[oaicite:6]{index=6}

- `eliminar_stopwords.py`  
  Elimina *stopwords* de los documentos usando una función **recursiva**
  (`eliminar_stopwords_recursivo`). Además, durante la ejecución **muestra por consola**
  las stopwords eliminadas en cada línea. :contentReference[oaicite:7]{index=7}

- `stopwords.txt`  
  Lista de palabras vacías (*stopwords*) en inglés que se desean eliminar del índice
  (artículos, preposiciones, pronombres, etc.). :contentReference[oaicite:8]{index=8}

- `build_index.awk`  
  Script AWK que construye el **índice invertido** a partir de los archivos sin stopwords
  (`data_clean/`). Para cada palabra crea un archivo `index/<palabra>.txt` que contiene
  la lista de documentos donde aparece esa palabra.

- `motor_busqueda.py`  
  Carga en memoria el índice invertido desde la carpeta `index/` y permite hacer consultas
  de múltiples palabras. La intersección de las listas de documentos se realiza de forma
  **recursiva** mediante la función `intersectar_recursivo`. :contentReference[oaicite:9]{index=9}

- `Makefile`  
  Automatiza la ejecución de los pasos anteriores mediante las reglas `prepare`, `clean_data`,
  `index`, `run` y `clean`. :contentReference[oaicite:10]{index=10}

- `videoGames.csv`  
  Dataset original (Kaggle) con información de videojuegos (nombre, descripción, ranking, etc.).

REQUISITOS
----------
- Python 3 instalado (`python` o `py`).
- AWK (por ejemplo, el que viene con Git Bash en Windows).
- `make` (por ejemplo, el que viene con Git/Git Bash).

USO (PASO A PASO)
-----------------

> Recomendación: en Windows usar **Git Bash** para ejecutar estos comandos.

1. Generar documentos `.txt` desde el CSV

    ```bash
    make prepare
    ```

   - Entrada: `videoGames.csv` (dataset de videojuegos).
   - Salida: múltiples archivos `.txt` en la carpeta `data/`
     con la descripción de cada videojuego. :contentReference[oaicite:11]{index=11}

2. Eliminar stopwords (con recursividad y mensajes en consola)

    ```bash
    make clean_data
    ```

   - Entrada: archivos `data/*.txt`.
   - Proceso:
     - Para cada línea del archivo, se aplican:
       - `eliminar_stopwords_recursivo(words, removed)` → función recursiva.
       - Se imprimen por consola las stopwords removidas en esa línea.
   - Salida: archivos limpios en la carpeta `data_clean/`.

   Ejemplo de mensaje en consola (salida aproximada):

