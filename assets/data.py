import pandas as pd
import re
from tkinter import filedialog
import os

SIMBOLS_REGEX = re.compile(r'^SIMBOLO\.?\d*$')
ROLLER_REGEX = re.compile(r'^R\d+$')

def process_excel(file_name):
    try:
        DATOS = pd.read_excel(file_name, sheet_name=1)

        SIMBOLS = list(filter(SIMBOLS_REGEX.match, DATOS.columns.values))
        ROLLERS = list(filter(ROLLER_REGEX.match, DATOS.columns.values))

    except FileNotFoundError:
        print(f"La ruta del archivo no existe: {file_name}")
    except Exception as e:
        print(f"Error al procesar {file_name}: {str(e)}")
    else:
        print(f"Procesado {file_name} correctamente")

        # Define file paths to save the JSON files
        simbols_path = os.path.splitext(file_name)[0] + '_simbols.json'
        rollers_path = os.path.splitext(file_name)[0] + '_rollers.json'

        # Save JSON files
        DATOS.loc[:, SIMBOLS].to_json(simbols_path, orient='records', indent=4)
        DATOS.loc[:, ROLLERS].to_json(rollers_path, orient='records', indent=4)

        return simbols_path, rollers_path

file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.xlsx")])
simbols, rollers = process_excel(file_path)

print(f"Simbols saved to: {simbols}")
print(f"Rollers saved to: {rollers}")
