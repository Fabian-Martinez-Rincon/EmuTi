import pandas as pd
import random
import string
import os
from tkinter import messagebox

def process_txt(nombre_archivo_txt):

    with open(nombre_archivo_txt, 'r') as archivo:
        lineas_txt = [linea.strip() for linea in archivo]

    simbolos = [random.choice(string.ascii_uppercase) for _ in range(len(lineas_txt))]

    datos = {'SIMBOLO': simbolos,
            'R1': lineas_txt}

    df = pd.DataFrame(datos)

    
    ruta_base, _ = os.path.splitext(nombre_archivo_txt)

    nombre_archivo_excel = f"{ruta_base}Procesado.xlsx"


    print(nombre_archivo_txt)
    PATH_BASE = os.path.dirname(nombre_archivo_txt)

    processed_path = os.path.join(PATH_BASE, nombre_archivo_excel)

    df.to_excel(processed_path, index=False)
    
    messagebox.showinfo("info", "Archivo procesado con exito")