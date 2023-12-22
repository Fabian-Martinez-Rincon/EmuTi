import tkinter as tk
from tkinter import filedialog
import re
import pandas as pd

SIMBOLS_REGEX = re.compile(r'^SIMBOLO\.\d+$')
ROLLER_REGEX = re.compile(r'^R\d+$')

def process_excel(file_name):
    try:
        DATOS = pd.read_excel(file_name,sheet_name=1)
        SIMBOLS = list(filter(SIMBOLS_REGEX.match, DATOS.columns.values))
        ROLLERS = list(filter(ROLLER_REGEX.match, DATOS.columns.values))
        
    except FileNotFoundError:
        print(f"La ruta del archivo no existe: {file_name}")
    except KeyError:
        print(f"Columnas no corresponden con {DATOS.columns.values}")
    except Exception as e:
        print(f"Error al procesar {file_name}: {str(e)}")
    else:
        print(f"Procesado {file_name} correctamente")
        return DATOS.loc[:, SIMBOLS].to_json(orient='records', indent=4), DATOS.loc[:, ROLLERS].to_json(orient='records', indent=4)
    

class MainGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.grid()
        self.create_widgets()

        self.simbols = None
        self.rollers = None

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.xlsx")])
        try:
            self.simbols, self.rollers = process_excel(file_path)
            print(self.simbols)
        except FileNotFoundError:
            print("La ruta no existe ", file_path)
        except NotADirectoryError:
            print("La ruta no es un directorio ", file_path)

    def show_window_value(self):
        window_value = self.window_entry.get()
        print(f"Valor de la ventana: {window_value}")

    def show_numeric_value(self):
        numeric_value = self.value_entry.get()
        print(f"Valor numérico: {numeric_value}")

    def toggle_automatic(self):
        print("Cambio de estado")
        current_state = self.auto_var.get()
        new_state = not current_state
        self.auto_var.set(new_state)
        self.update_auto_button()

    def update_auto_button(self):
        if not self.auto_var.get():
            print("Automático ON")
            self.auto_on_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
            self.auto_off_button.grid_remove()
        else:
            print("Automático OFF")
            self.auto_on_button.grid_remove()
            self.auto_off_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    def next_step(self):
        self.result_label.config(text="Siguiente paso")

    def create_widgets(self):
        self.file_button = tk.Button(self, text="Seleccionar Archivo", command=self.open_file_dialog)
        self.file_button.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        self.auto_var = tk.BooleanVar()

        self.auto_on_button = tk.Button(self, text="▶️", command=self.toggle_automatic)
        self.auto_on_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

        self.auto_off_button = tk.Button(self, text="⏸️", command=self.toggle_automatic)
        self.auto_off_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
        self.auto_off_button.grid_remove()

        self.next_button = tk.Button(self, text="Siguiente", command=self.next_step)
        self.next_button.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

        self.window_label = tk.Label(self, text="Nombre de la ventana:")
        self.window_label.grid(row=4, column=0, pady=10, padx=10)

        self.window_entry = tk.Entry(self)
        self.window_entry.grid(row=5, column=0, pady=10, padx=10)

        self.show_window_button = tk.Button(self, text="Mostrar Valor", command=self.show_window_value)
        self.show_window_button.grid(row=5, column=1, pady=10, padx=10)

        self.value_label = tk.Label(self, text="Valor numérico:")
        self.value_label.grid(row=6, column=0, pady=10, padx=10)

        self.value_entry = tk.Entry(self)
        self.value_entry.grid(row=7, column=0, pady=10, padx=10)

        self.show_numeric_button = tk.Button(self, text="Mostrar Valor", command=self.show_numeric_value)
        self.show_numeric_button.grid(row=7, column=1, pady=10, padx=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=8, column=0, pady=10, padx=10, columnspan=2)

        self.close_button = tk.Button(self, text="Cerrar", command=self.master.destroy)
        self.close_button.grid(row=9, column=0, pady=10, padx=10, columnspan=2)
