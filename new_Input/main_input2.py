import tkinter as tk
import pygetwindow as gw
import pyautogui

INDICE = 0
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
    }
]

TITULO_BASE = "Ingreso de Datos"

index = 0

def activar_ventana(boton, result_label, auto = None):
    """Espera a que se abra la ventana y la activa"""
    ventana = None
    global index

    def buscar_ventana():
        nonlocal ventana
        global index
        try:
            ventana = gw.getWindowsWithTitle(TITULO_BASE)[0]
            if ventana.isMinimized:
                ventana.restore()

            ventana.activate()
            boton.config(state=tk.NORMAL)
            
            values = ",".join(
                str(value) for value in ROLLERS[index].values()
                )

            print(values)
            result_label.config(text=values)

            pyautogui.press('tab')
            pyautogui.press('tab')

            pyautogui.write(values)
            pyautogui.press('enter')

        except IndexError:
            result_label.config(text="No se encontro la ventana")
    
    boton.config(state=tk.DISABLED)
    result_label.config(text="Buscando ventana")

    buscar_ventana()

    if index < len(ROLLERS):
        if ventana is None:
            result_label.after(1000, activar_ventana, boton, result_label) 
        else:
            index += 1
    else:
        boton.config(state=tk.DISABLED)            
        result_label.config(text="Terminado")