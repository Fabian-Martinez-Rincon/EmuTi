import re
import pandas as pd
import os
import json
from tkinter import messagebox

SIMBOLS_REGEX = re.compile(r'^SIMBOLO\.?\d*$')
ROLLER_REGEX = re.compile(r'^R\d+$')

PATH_BASE = os.path.dirname(os.path.dirname(__file__))

def json_process(data, simbols, rollers):
    
    SIMBOLS_JSON = data.loc[:, simbols].to_json(orient='records', indent=4)
    ROLLERS_JSON = data.loc[:, rollers].to_json(orient='records', indent=4)
        
    simbols_data = json.loads(SIMBOLS_JSON)
    rollers_data = json.loads(ROLLERS_JSON)

    index_null_simbols = [
        index for index, item in enumerate(simbols_data)
        if any(value is None for value in item.values())
        ]
    
    index_null_rollers = [
        index for index, item in enumerate(rollers_data)
        if any(value is None for value in item.values())
        ]

    if len(index_null_rollers) > 0:
        messagebox.showwarning("Error", f"Indices con valor nulo en R {index_null_rollers}")
        return "", ""

    if len(index_null_simbols) > 0:
        messagebox.showwarning("Error", f"Indices con valor nulo SIMBOL {index_null_simbols}")
        return "", ""

    messagebox.showinfo("info", "CARGA EXITOSA")
    return SIMBOLS_JSON, ROLLERS_JSON

def process_excel(file_name):
    SIMBOLS_JSON = None
    ROLLERS_JSON = None
    
    try:
        DATOS = pd.read_excel(file_name, sheet_name=0)
        values = DATOS.columns.values
        print(values)
        SIMBOLS = list(filter(SIMBOLS_REGEX.match, values))
        ROLLERS = list(filter(ROLLER_REGEX.match, values))

        SIMBOLS_JSON, ROLLERS_JSON = json_process(DATOS, SIMBOLS, ROLLERS)
        
    except PermissionError:
        print(f"El archivo {file_name} está abierto")
    except FileNotFoundError:
        print(f"La ruta del archivo no existe: {file_name}")
    except KeyError:
        print(f"Columnas no corresponden con el formato: {file_name}")
    except Exception as e:
        print(f"Error al procesar {file_name}: {str(e)}")
    else:
        print(f"Procesado {file_name} correctamente")
    
    return SIMBOLS_JSON, ROLLERS_JSON
