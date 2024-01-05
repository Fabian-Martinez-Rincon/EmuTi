import pandas as pd
import random
import string

# Nombre del archivo de texto
nombre_archivo_txt = 'jugadas.txt'

# Leer las líneas del archivo y almacenarlas en una lista
with open(nombre_archivo_txt, 'r') as archivo:
    lineas_txt = [linea.strip() for linea in archivo]

# Generar letras aleatorias para el campo 'SIMBOLO'
simbolos = [random.choice(string.ascii_uppercase) for _ in range(len(lineas_txt))]

# Crear un DataFrame con las líneas del archivo y letras aleatorias en la columna 'SIMBOLO'
datos = {'SIMBOLO': simbolos,
         'R1': lineas_txt}

df = pd.DataFrame(datos)

# Nombre del archivo Excel
nombre_archivo_excel = 'mi_excel.xlsx'

# Guardar el DataFrame en un archivo Excel
df.to_excel(nombre_archivo_excel, index=False)

print(f'Se ha creado el archivo Excel: {nombre_archivo_excel}')

