import pandas as pd
import os

ruta_directorio = 'C:/Users/benja/Documents/Particulas_contaminantes_chillan/data/raw/datos_direccion_meteorologica/precipitaciones/'

# Función para procesar cada archivo y retornar el DataFrame procesado
def procesar_archivo(nombre_archivo):
    df = pd.read_excel(os.path.join(ruta_directorio, nombre_archivo), engine='openpyxl', header=None, skiprows=2, usecols="B:M", nrows=31)

    fechas = []
    mediciones = []

# Iterar sobre las celdas del dataframe
    for columna in range(df.shape[1]):
        for fila in range(df.shape[0]):
            # Generar la fecha a partir del nombre del archivo y la posición de la celda
            fecha = f"{nombre_archivo.split('.')[0]}-{columna+1:02}-{fila+1:02}"
            valor = df.iloc[fila, columna]  # Aquí estaba el error
            medicion = 0 if valor == "s/p" else valor
            fechas.append(fecha)
            mediciones.append(medicion)


    # Crear un nuevo DataFrame con las fechas y mediciones y retornarlo
    df_salida = pd.DataFrame({'Fecha': fechas, 'Medicion': mediciones})
    return df_salida

# Lista para almacenar los DataFrames de cada archivo
dataframes = []

for archivo in os.listdir(ruta_directorio):
    if archivo.endswith('.xlsx'):
        print(f"Procesando {archivo}...")
        df_actual = procesar_archivo(archivo)
        dataframes.append(df_actual)

# Concatenar todos los DataFrames en uno solo
df_final = pd.concat(dataframes)

# Guardar el DataFrame final en un solo archivo CSV
nombre_salida = "datos_concatenados_procesados.csv"
df_final.to_csv(os.path.join(ruta_directorio, nombre_salida), index=False)

