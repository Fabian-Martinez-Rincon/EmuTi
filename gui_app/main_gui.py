import tkinter as tk
from tkinter import filedialog
import re
import pandas as pd
#from new_Input.main_input import manual_mode
from new_Input.main_input import automatic_mode
import pygetwindow as gw
import pyautogui
import time



SIMBOLS_REGEX = re.compile(r'^SIMBOLO\.\d+$')
ROLLER_REGEX = re.compile(r'^R\d+$')

ROLLERS = [
    {
        "R1":1,
        "R2":6,
        "R3":8,
        "R4":2,
        "R5":6
    },
    {
        "R1":3,
        "R2":17,
        "R3":4,
        "R4":2,
        "R5":10
    },
    {
        "R1":3,
        "R2":17,
        "R3":4,
        "R4":2,
        "R5":12
    },
        {
        "R1":1,
        "R2":6,
        "R3":8,
        "R4":2,
        "R5":6
    },
    {
        "R1":3,
        "R2":17,
        "R3":4,
        "R4":2,
        "R5":10
    },
    {
        "R1":3,
        "R2":17,
        "R3":4,
        "R4":2,
        "R5":12
    }
]
SIMBOLS = [ 
    {
        "SIMBOLO.1":"S0",
        "SIMBOLO.2":"B2",
        "SIMBOLO.3":"SK",
        "SIMBOLO.4":"B2"
    },
    {
        "SIMBOLO.1":"S0",
        "SIMBOLO.2":"B2",
        "SIMBOLO.3":"SK",
        "SIMBOLO.4":"B1"
    },
    {
        "SIMBOLO.1":"S0",
        "SIMBOLO.2":"B1",
        "SIMBOLO.3":"SK",
        "SIMBOLO.4":"B2"
    },
    {
        "SIMBOLO.1":"S0",
        "SIMBOLO.2":"B2",
        "SIMBOLO.3":"SK",
        "SIMBOLO.4":"B2"
    },
    {
        "SIMBOLO.1":"S0",
        "SIMBOLO.2":"B2",
        "SIMBOLO.3":"SK",
        "SIMBOLO.4":"B1"
    },
    {
        "SIMBOLO.1":"S0",
        "SIMBOLO.2":"B1",
        "SIMBOLO.3":"SK",
        "SIMBOLO.4":"B2"
    }
]

def search_window():
        """Busca la ventana y la activa"""
        ventana = None
        try:
            ventana = gw.getWindowsWithTitle("Ingreso de Datos")[0]
        except IndexError:
            return False
        
        if ventana.isMinimized:
            ventana.restore()

        ventana.activate()
        return True

def actions(result_label, indice):

    values = ",".join(str(value) for value in ROLLERS[indice].values())
    print(f"Index {indice}: {values}")
    result_label.config(text=f"Index {indice}: {values}")

    pyautogui.press('tab')
    pyautogui.write(values)
    pyautogui.press('enter')

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
        self.index_current = 0
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
        self.auto_var.set(not self.auto_var.get())
        
        if not self.auto_var.get():
            print("Automático OFF")
            self.auto_on_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
            self.auto_off_button.grid_remove()
        else:
            print("Automático ON")
            
            self.auto_on_button.grid_remove()
            self.auto_off_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
        
    # def activate_auto(self):
    #     print("Automático ON")
    #     #automatic_mode(self.next_button, self.result_label_rollers)

    # def deactivate_auto(self):
    #     print("Automático OFF")

    def activate_auto(self):
        self.auto_var.set(1)  # Activar el botón "Activar"
        print("Automático ON")
        self.auto_on_button.config(state=tk.DISABLED)
        self.auto_off_button.config(state=tk.NORMAL)

    def deactivate_auto(self):
        self.auto_var.set(0)  # Activar el botón "Desactivar"
        print("Automático OFF")
        self.auto_on_button.config(state=tk.NORMAL)
        self.auto_off_button.config(state=tk.DISABLED)
        

    def next_step(self):
        self.result_label_rollers.config(text="Siguiente paso")

    def press_button_manual(self, next_button):
        """Manual 
            El boton esta desactivado por defecto hasta que encuentre la ventana
            Si tiene elementos, ejecuto la accion y actualizo los datos
            En caso contrario, le muestro en terminar

            - Despues de un segundo, el boton solo se desactiva cuando se 
              encuentra activada la ventana
        """

        next_button.config(state=tk.DISABLED)         
        index = self.index_current
        while not search_window():
            time.sleep(1)
            pass
        

        if index < len(ROLLERS):
            actions(self.result_label_rollers, index)
            self.index_current += 1
            self.update_index_label()
        else:
            self.result_label_rollers.config(text="Terminado")

        self.master.after(1000, lambda: self.enable_button(next_button))

    def enable_button(self, next_button):
        while not search_window():
            time.sleep(1)
            pass
        next_button.config(state=tk.NORMAL)

    def create_widgets(self):

        button_style = {"font": ("Helvetica", 10), "bd": 2, "relief": tk.GROOVE}

        self.file_button = tk.Button(self, text="SELECCIONAR ARCHIVO", command=self.open_file_dialog, **button_style)
        self.file_button.grid(row=0, column=2, pady=10, padx=10, columnspan=2)

        self.auto_var = tk.BooleanVar()

        self.auto_title_label = tk.Label(self, text="AUTOMATICO", font=("Helvetica", 12, "bold"), bg="#add8e6")
        self.auto_title_label.grid(row=1, column=2, pady=10, padx=10, columnspan=2)

        self.auto_on_button = tk.Button(self, text="ACTIVAR", command=self.activate_auto, **button_style)
        self.auto_on_button.grid(row=2, column=1, pady=10, padx=10, columnspan=2)
        self.auto_on_button.config(state=tk.NORMAL) 

        self.auto_off_button = tk.Button(self, text="DESACTIVAR", command=self.deactivate_auto, **button_style)
        self.auto_off_button.grid(row=2, column=3, pady=10, padx=10, columnspan=2)
        self.auto_off_button.config(state=tk.DISABLED)

        self.auto_on_button["state"] = "disabled"
        self.auto_off_button["state"] = "active"
        
        self.auto_title_label = tk.Label(self, text="Tradicional", font=("Helvetica", 12, "bold"), bg="#add8e6")
        self.auto_title_label.grid(row=3, column=2, pady=10, padx=10, columnspan=2)

        self.next_button = tk.Button(self, text="SIGUIENTE", command=lambda: self.press_button_manual(self.next_button), **button_style)
        self.next_button.grid(row=4, column=2, pady=10, padx=10, columnspan=2)

        self.window_label = tk.Label(self, text="VENTANA:", bg="#add8e6")
        self.window_label.grid(row=5, column=0, pady=10, padx=10, columnspan=2)

        self.window_entry = tk.Entry(self)
        self.window_entry.grid(row=5, column=2, pady=10, padx=10 , columnspan=2)

        self.show_window_button = tk.Button(self, text="Confirmar", command=self.show_window_value, **button_style)
        self.show_window_button.grid(row=5, column=4, pady=10, padx=10, columnspan=2)

        self.custom_index_label = tk.Label(self, text="COLUMNA EXCEL:", bg="#add8e6")
        self.custom_index_label.grid(row=6, column=0, pady=10, padx=10 , columnspan=2)

        self.custom_index_entry = tk.Entry(self)
        self.custom_index_entry.grid(row=6, column=2, pady=10, padx=10, columnspan=2)

        self.update_custom_index_button = tk.Button(self, text="ACTUALIZAR", command=self.update_custom_index, **button_style)
        self.update_custom_index_button.grid(row=6, column=4, pady=10, padx=10 , columnspan=2)

        self.auto_title_label = tk.Label(self, text="DATOS CONFIRMADOS", font=("Helvetica", 12, "bold"), bg="#add8e6")
        self.auto_title_label.grid(row=7, column=2, pady=10, padx=10, columnspan=2)

        self.result_label_simbol = tk.Label(self, text="W, W, W, W, W")
        self.result_label_simbol.grid(row=8, column=1, pady=10, padx=10, columnspan=2)

        self.result_label_rollers = tk.Label(self, text="1, 1, 1, 1, 1")
        self.result_label_rollers.grid(row=8, column=3, pady=10, padx=10, columnspan=2)

        self.index_label = tk.Label(self, text=f"Índice Actual: {self.index_current}")
        self.index_label.grid(row=9, column=2, pady=10, padx=10, columnspan=2)

        self.close_button = tk.Button(self, text="Cerrar", command=self.master.destroy, **button_style)
        self.close_button.grid(row=10, column=2, pady=10, padx=10, columnspan=2)

        


    def update_index_label(self):
        self.index_label.config(text=f"Índice: {self.index_current}")

    def update_custom_index(self):
        try:
            new_index = int(self.custom_index_entry.get())
            self.index_current = new_index
            self.update_index_label()
        except ValueError:
            print("Ingrese un valor numérico para el índice personalizado.")