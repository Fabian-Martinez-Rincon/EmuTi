import re
import pandas as pd
import os

SIMBOLS_REGEX = re.compile(r'^SIMBOLO\.?\d*$')
ROLLER_REGEX = re.compile(r'^R\d+$')

PATH_BASE = os.path.dirname(os.path.dirname(__file__))

PATH_PROSSED = os.path.join(PATH_BASE, "processed_datasets")
if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)

PATH_SIMBOLS = os.path.join(PATH_PROSSED, "simbols.json")
PATH_ROLLERS = os.path.join(PATH_PROSSED, "rollers.json")

def process_excel(file_name):
    try:
        DATOS = pd.read_excel(file_name, sheet_name=1)
        values = DATOS.columns.values

        SIMBOLS = list(filter(SIMBOLS_REGEX.match, values))
        ROLLERS = list(filter(ROLLER_REGEX.match, values))

        SIMBOLS_JSON = DATOS.loc[:, SIMBOLS].to_json(orient='records', indent=4)
        ROLLERS_JSON = DATOS.loc[:, ROLLERS].to_json(orient='records', indent=4)
        
        with open(PATH_SIMBOLS, 'w') as f:
            f.write(SIMBOLS_JSON)
        
        with open(PATH_ROLLERS, 'w') as f:
            f.write(ROLLERS_JSON)
        
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

        
    