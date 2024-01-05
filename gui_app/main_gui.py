import tkinter as tk
from tkinter import filedialog
import pygetwindow as gw
import pyautogui
from tkinter import messagebox
from gui_app.data_process import process_excel
from gui_app._macros import *


def search_window(window, master):
        """Busca la ventana y la activa"""
        ventana = None
        try:
            ventana = gw.getWindowsWithTitle(window)[0]
        except IndexError:
            return False
        try:
            if ventana.isMinimized:
                ventana.restore()
            ventana.activate()
            return True
        except Exception as e:
            alert_except(master, "ERROR AL ACTIVAR LA VENTANA")
            return False
    
def transform_data(index, rollers, simbols):
    rollers = eval(rollers)
    rollers = ",".join(str(value) for value in rollers[index].values())

    simbols = eval(simbols)
    simbols = ",".join(str(value) for value in simbols[index].values())

    return rollers, simbols

def actions(result_label_rollers, result_label_simbol, indice, simbols, rollers):
    rollers, simbols = transform_data(indice, rollers, simbols)

    result_label_rollers.config(text=f"{rollers}")
    result_label_simbol.config(text=f"{simbols}")

    
    pyautogui.press('tab')
    pyautogui.write(rollers)
    pyautogui.press('enter')
    

class MainGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.index_current = 0
        self.window_current = ""
        self.grid()
        self.create_widgets()

        self.simbols = None
        self.rollers = None

        self.auto_var = tk.BooleanVar()
        self.auto_on_button.config(variable=self.auto_var)

        self.interval_id = None
        
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.xlsx")])
        try:
            self.simbols, self.rollers = process_excel(file_path)
        except FileNotFoundError:
            alert_except(self, "LA RUTA NO EXISTE")
        except NotADirectoryError:
            print("La ruta no es un directorio ", file_path)
        except ValueError as e:
            print(e)

    def press_button_manual(self, next_button):
        """Manual 
            El boton esta desactivado por defecto hasta que encuentre la ventana
            Si tiene elementos, ejecuto la accion y actualizo los datos
            En caso contrario, le muestro en terminar

            - Despues de un segundo, el boton solo se desactiva cuando se 
              encuentra activada la ventana
        """

        if not self.rollers:
            messagebox.showinfo("Error", "Seleccione un archivo")
            return
        
        if not self.window_current:
            messagebox.showinfo("Error","Ingrese una ventana")
            return
        
        if not search_window(self.window_current, self.master):
            alert_error(self,"VENTANA INACTIVA")
            return

        next_button.config(state=tk.DISABLED)
        index = self.index_current
        
        if index < len(self.rollers):
            try:
                actions(self.result_label_rollers, self.result_label_simbol, index, self.simbols, self.rollers)
            except Exception as e:
                alert_except(self, "EXCEPCION AL ESCRIBIR")
            else:
                self.index_current += 1
                self.update_index_label()
        else:
            self.result_label_rollers.config(text="Terminado")

        self.master.after(1000, lambda: self.enable_button(next_button))

    def enable_button(self, next_button):
        next_button.config(state=tk.NORMAL)

    def toggle_auto(self):
        if self.auto_var.get():
            self.interval_id = self.master.after(2000, self.press_button_auto)
            alert_success(self,"AUTO INICIADO")
        else:
            if self.interval_id:
                self.master.after_cancel(self.interval_id)
                self.interval_id = None
                alert_success(self,"AUTO DETENIDO")

    def press_button_auto(self):
        self.press_button_manual(self.next_button)
        self.interval_id = self.master.after(2000, self.press_button_auto)

    def create_widgets(self):

        button_style = {"font": ("Helvetica", 10), "bd": 2, "relief": tk.GROOVE}

        self.file_button = tk.Button(self, text="SELECCIONAR ARCHIVO", command=self.open_file_dialog, **button_style)
        self.file_button.grid(row=0, column=0, pady=10, padx=10, columnspan=5)

        title_style(self, "AUTOMATICO", 1, 0)

        self.auto_on_button = tk.Checkbutton(self, text="ACTIVAR", command=self.toggle_auto)
        self.auto_on_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
        
        title_style(self, "MANUAL", 1, 2)
        
        self.next_button = tk.Button(self, text="INGRESAR", command=lambda: self.press_button_manual(self.next_button), **button_style)
        self.next_button.grid(row=2, column=2, pady=10, padx=10, columnspan=2)

        self.window_label = tk.Label(self, text="VENTANA", bg="#add8e6")
        self.window_label.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

        self.window_entry = tk.Entry(self)
        self.window_entry.grid(row=4, column=0, pady=10, padx=10 , columnspan=2)

        self.show_window_button = tk.Button(self, text="Confirmar", command=self.update_window_index, **button_style)
        self.show_window_button.grid(row=5, column=0, pady=10, padx=10, columnspan=2)

        self.custom_index_label = tk.Label(self, text="INDICE NUEVO", bg="#add8e6")
        self.custom_index_label.grid(row=3, column=2, pady=10, padx=10 , columnspan=2)

        self.custom_index_entry = tk.Entry(self)
        self.custom_index_entry.grid(row=4, column=2, pady=10, padx=10, columnspan=2)

        self.update_custom_index_button = tk.Button(self, text="ACTUALIZAR", command=self.update_custom_index, **button_style)
        self.update_custom_index_button.grid(row=5, column=2, pady=10, padx=10 , columnspan=2)

        self.auto_title_label = tk.Label(self, text="DATOS INGRESADOS", bg="#add8e6")
        self.auto_title_label.grid(row=6, column=0, pady=10, padx=10, columnspan=2)

        self.result_label_simbol = tk.Label(self, text="W, W, W, W, W")
        self.result_label_simbol.grid(row=7, column=0, pady=10, padx=10, columnspan=2)

        self.result_label_rollers = tk.Label(self, text="1, 1, 1, 1, 1")
        self.result_label_rollers.grid(row=8, column=0, pady=10, padx=10, columnspan=2)
        
        self.auto_title_label = tk.Label(self, text="INDICE DATOS", bg="#add8e6")
        self.auto_title_label.grid(row=6, column=2, pady=10, padx=10, columnspan=2)

        self.result_label_simbol2 = tk.Label(self, text="W, W, W, W, W")
        self.result_label_simbol2.grid(row=7, column=2, pady=10, padx=10, columnspan=2)

        self.result_label_rollers2 = tk.Label(self, text="1, 1, 1, 1, 1")
        self.result_label_rollers2.grid(row=8, column=2, pady=10, padx=10, columnspan=2)

        self.index_label = tk.Label(self, text=f"INDICE : {self.index_current}")
        self.index_label.grid(row=9, column=0, pady=10, padx=10, columnspan=5)

        self.file_button = tk.Button(self, text="SELECCIONAR ARCHIVO", command=self.open_file_dialog, **button_style)
        self.file_button.grid(row=0, column=0, pady=10, padx=10, columnspan=5)

        self.close_button = tk.Button(self, text="CERRAR", command=self.master.destroy, **button_style)
        self.close_button.grid(row=11, column=0, pady=10, padx=10, columnspan=5)

    def update_window_label(self):
        self.window_label.config(text=f"{self.window_current}")

    def update_window_index(self):
        try:
            new_window = str(self.window_entry.get())
            self.window_current = new_window
            self.update_window_label()
        except ValueError:
            print("Ingrese un valor String para la ventana.")

    def update_index_label(self):
        self.index_label.config(text=f"Índice: {self.index_current}")

    def update_custom_index(self):
        try:
            new_index = int(self.custom_index_entry.get())
            self.index_current = new_index
            rollers, simbols = transform_data(self.index_current, self.rollers, self.simbols)
            self.result_label_rollers2.config(text=f"{rollers}")
            self.result_label_simbol2.config(text=f"{simbols}")
            self.update_index_label()
        except ValueError:
            print("Ingrese un valor numérico para el índice personalizado.")