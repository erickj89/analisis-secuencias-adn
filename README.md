# Análisis de secuencias nucleotídicas

 Análisis básico de secuencias nucleotídicas utilizando Python.

 ## Descripcion

Este proyecto analiza secuencias nucleotídicas de cuatro genes humanos:
TP53, BRCA1, EGFR y KRAS.

El programa calcula la longitud de cada secuencia, la cantidad de
nucleótidos A, T, C y G, y el porcentaje de contenido GC.

Las secuencias se obtuvieron de NCBI en formato FASTA.

## Estructura del proyecto

- `datos/`: contiene las cuatro secuencias descargadas de NCBI en formato FASTA.
- `scripts/`: contiene el programa `analisis_adn.py`.
- `resultados/`: contiene el archivo `resumen.csv` con los resultados del análisis.
- `README.md`: documentación del proyecto.
- `LICENSE`: licencia del repositorio.
- `.gitignore`: indica qué archivos debe ignorar Git.

## Ejecución del programa

Para ejecutar el análisis es necesario tener Python 3 instalado.

1. Descargar el repositorio de GitHub.
2. Abrir una terminal en la carpeta principal del proyecto.
3. Ejecutar el siguiente comando:

```
python scripts/analisis_adn.py
```

El programa analiza las cuatro secuencias FASTA, muestra los resultados en la terminal y genera el archivo resultados/resumen.csv.

## Origen de los datos

Las secuencias utilizadas en este proyecto se obtuvieron de la base de datos NCBI (National Center for Biotechnology Information).

Se utilizaron secuencias de referencia de ARN mensajero (mRNA) de cuatro genes humanos:

- **TP53:** NM_000546.6
- **BRCA1:** NM_007294.4
- **EGFR:** NM_005228.5
- **KRAS:** NM_004985.5

Los archivos se descargaron en formato FASTA y se almacenaron en la carpeta datos/.

Fuente: https://www.ncbi.nlm.nih.gov/
