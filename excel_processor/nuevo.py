import pandas as pd
import os
import re

SIMBOLS_REGEX = re.compile(r'^SIMBOLO\.\d+$')
ROLLER_REGEX = re.compile(r'^R\d+$')

variable = "C:/Users/Fabian/Desktop/Fortuna.xlsx"

def process_excel(file_name):
    try:
        DATOS = pd.read_excel(file_name,sheet_name=1)
        SIMBOLS = list(filter(SIMBOLS_REGEX.match, DATOS.columns.values))
        ROLLERS = list(filter(ROLLER_REGEX.match, DATOS.columns.values))

        DATOS_FILTRADOS = DATOS.loc[:, 
            (SIMBOLS + ROLLERS)
        ].to_json(orient='records', indent=4)

    except FileNotFoundError:
        print(f"La ruta del archivo no existe: {file_name}")
    except KeyError:
        print(f"Columnas no corresponden con {DATOS.columns.values}")
    except Exception as e:
        print(f"Error al procesar {file_name}: {str(e)}")
    else:
        print(f"Procesado {file_name} correctamente")


if __name__ == "__main__":
    try:
        process_excel(variable)
    except FileNotFoundError:
        print("La ruta no existe ", variable)
    except NotADirectoryError:
        print("La ruta no es un directorio ", variable)