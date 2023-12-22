import tkinter as tk
import pygetwindow as gw
import pyautogui

TITULO_BASE = "Ingreso de Datos"
INDICE = 0

DATA = [
    {"SIMBOLO": "W", "SIMBOLO.1": "W", "SIMBOLO.2": "W", "SIMBOLO.3": "W", "SIMBOLO.4": "W", "R1": 3, "R2": 6, "R3": 8, "R4": 32, "R5": 5},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "F", "SIMBOLO.4": "F", "R1": 4, "R2": 11, "R3": 23, "R4": 5, "R5": 12},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "F", "SIMBOLO.4": "W", "R1": 4, "R2": 11, "R3": 23, "R4": 5, "R5": 5},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "W", "SIMBOLO.4": "F", "R1": 4, "R2": 11, "R3": 23, "R4": 32, "R5": 12},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "W", "SIMBOLO.4": "W", "R1": 4, "R2": 11, "R3": 23, "R4": 32, "R5": 5}
]

CAMPOS = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']

def activar_ventana(boton):
    """Espera a que se abra la ventana y la activa"""
    while True:
        try:
            ventana = gw.getWindowsWithTitle(TITULO_BASE)[0]
            ventana.activate()
            boton.config(state=tk.NORMAL)
            return ventana
        except IndexError:
            pass


def mostrar_registro(datos, boton):
    global INDICE
    global VENTANA

    registro = datos[INDICE]
    valores = [registro[campo] for campo in CAMPOS]

    r_valores_text = ", ".join(str(valores[i]) for i, campo in enumerate(CAMPOS) if campo.startswith('R'))
    simbolo_valores_text = ", ".join(str(valores[i]) for i, campo in enumerate(CAMPOS) if campo.startswith('SIMBOLO'))

    print('Datos Confirmados:')
    print('INDICE: ' + str(INDICE))
    print(r_valores_text)
    print(simbolo_valores_text)


    widgets = VENTANA.children.values()
    
    # Buscar el único Label en la ventana
    label_ventana = next(widget for widget in widgets if isinstance(widget, tk.Label))
    
    label_ventana.focus_set()  # Establecer enfoque en el Label

    pyautogui.write(str(r_valores_text))
    pyautogui.press('enter')

    boton.config(state=tk.DISABLED)
    activar_ventana(boton)
    INDICE += 1

def click_boton(datos, boton):
    boton.config(state=tk.DISABLED)
    VENTANA = activar_ventana(boton)
    mostrar_registro(datos, boton)

def main():
    root = tk.Tk()
    boton = tk.Button(root, text='Siguiente', command=lambda: click_boton(DATA, boton))
    boton.grid(row=1, column=0, columnspan=2)

    boton.config(state=tk.DISABLED)  # Inicialmente, el botón está deshabilitado
    VENTANA = activar_ventana(boton)
    root.mainloop()
    

if __name__ == '__main__':
    main()
