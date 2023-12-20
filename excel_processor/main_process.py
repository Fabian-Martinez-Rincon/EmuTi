import pandas as pd
import os

PATH_BASE = os.path.dirname(os.path.abspath(__file__))
PATH_SOURCE = os.path.join(PATH_BASE, "base_excel")
PATH_PROSSED = os.path.join(PATH_BASE, "processed_json")

if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)

def process_excel(file_name, sheet_number, columns_to_select):
    try:
        file_path = os.path.join(PATH_SOURCE, file_name)
        DATOS = pd.read_excel(file_path,sheet_name=sheet_number)
        DATOS_FILTRADOS = DATOS.loc[:, 
            columns_to_select
        ].to_json(orient='records', indent=4)

        with open(os.path.join(PATH_PROSSED, file_name.replace(".xlsx", ".json")), 'w') as archivo:
            archivo.write(DATOS_FILTRADOS)

    except FileNotFoundError:
        print(f"La ruta del archivo no existe: {file_name}")
    except KeyError:
        print(f"Columnas no corresponden con {DATOS.columns.values}")
    except Exception as e:
        print(f"Error al procesar {file_name}: {str(e)}")
    else:
        print(f"Procesado {file_name} correctamente")

if __name__ == "__main__":
    sheet_number = 1
    columns_to_select = [
        'SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 
        'R1', 'R2', 'R3', 'R4', 'R5'
    ]

    try:
        names_files = os.listdir(PATH_SOURCE)
        for file_name in names_files:
            process_excel(file_name, sheet_number, columns_to_select)
    except FileNotFoundError:
        print("La ruta no existe ", PATH_SOURCE)
    except NotADirectoryError:
        print("La ruta no es un directorio ", PATH_SOURCE)