# Análisis Comparativo de Diferentes Algoritmos Basados en Deep Learning para la Predicción de Fuentes Contaminantes (PM2.5 y PM10) en la Localidad de Chillán

## Descripción
Este proyecto se enfoca en el análisis comparativo de varios algoritmos de Deep Learning para predecir niveles de contaminantes (PM2.5 y PM10) en Chillán. Se utilizan datos meteorológicos y de calidad del aire para evaluar el desempeño de diferentes modelos predictivos.

## Tecnologías
- Python 3.11.4
- Otras dependencias se encuentran en `requirements.txt`.

## Datos
- Datos meteorológicos obtenidos de la Dirección Meteorológica de Chile.
- Datos de PM10 y PM2.5 de SINCA.
- Los datos están organizados en carpetas: `raw` para datos sin procesar y `processed` para datos procesados.

## Estructura del Repositorio
- `scrub_and_obtain/`: Scripts para obtener y limpiar los datos.
- `explore/`: Análisis exploratorio de datos y generación de estadísticas predictivas. Se incluyen imágenes de los análisis.
- `model/`: Implementación y evaluación de algoritmos de Deep Learning. Cada algoritmo tiene un archivo Excel asociado con los resultados de diferentes ejecuciones.
- `lluvia.py`: Script para generar datos sobre precipitaciones.
- `dataset.ipynb`: Notebook para la creación del dataset completo.

## Instalación
Para instalar las dependencias, ejecuta: pip install -r requirements.txt
