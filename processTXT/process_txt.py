"""
Este módulo procesa un archivo de texto, genera una lista de símbolos aleatorios para cada línea,
y guarda los resultados en un archivo Excel.

La función `process_txt` lee el archivo de texto proporcionado, genera una lista de símbolos
aleatorios
en mayúsculas del alfabeto inglés, y guarda estos datos junto con las líneas originales en un 
archivo Excel.
"""

import os
import random
import string
from tkinter import messagebox
import pandas as pd

def process_txt(nombre_archivo_txt):
    """
    Procesa un archivo de texto para generar un archivo Excel con símbolos aleatorios.

    Lee un archivo de texto línea por línea, genera un símbolo aleatorio en mayúscula del alfabeto 
    inglés
    para cada línea, y guarda estos datos junto con las líneas originales en un archivo Excel en la
    misma
    ubicación que el archivo de texto.

    Args:
        nombre_archivo_txt (str): Ruta del archivo de texto a procesar.

    Returns:
        None
    """
    with open(nombre_archivo_txt, 'r', encoding='utf-8') as archivo:
        lineas_txt = [linea.strip() for linea in archivo]

    simbolos = [random.choice(string.ascii_uppercase) for _ in range(len(lineas_txt))]
    datos = {'SIMBOLO': simbolos,
            'R1': lineas_txt}

    df = pd.DataFrame(datos)
    ruta_base, _ = os.path.splitext(nombre_archivo_txt)
    nombre_archivo_excel = f"{ruta_base}Procesado.xlsx"

    print(nombre_archivo_txt)
    path_base = os.path.dirname(nombre_archivo_txt)
    processed_path = os.path.join(path_base, nombre_archivo_excel)
    df.to_excel(processed_path, index=False)
    messagebox.showinfo("info", "Archivo procesado con exito")
