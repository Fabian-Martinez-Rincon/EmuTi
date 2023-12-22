import tkinter as tk
import pygetwindow as gw
import pyautogui


import tkinter as tk
import json
import pygetwindow as gw
import pyautogui
import os

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

def activar_ventana(boton, result_label):
    """Espera a que se abra la ventana y la activa"""
    ventana = None
    
    def buscar_ventana():
        nonlocal ventana
        try:
            ventana = gw.getWindowsWithTitle(TITULO_BASE)[0]
            if ventana.isMinimized:
                ventana.restore()

            ventana.activate()
            boton.config(state=tk.NORMAL)
            print("Numeros")
            result_label.config(text="Siguiente paso")
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.write(str("123"))
            pyautogui.press('enter')

        except IndexError:
            result_label.config(text="No se encontro la ventana")
    
    boton.config(state=tk.DISABLED)
    result_label.config(text="Buscando ventana")

    buscar_ventana()
    if ventana is None:
        result_label.after(1000, activar_ventana, boton, result_label) 
    

def main():
    root = tk.Tk()
    result_label = tk.Label(text="")
    result_label.grid(row=7, column=0, pady=10, padx=10, columnspan=2)
    boton = tk.Button(root, text='Siguiente', command=lambda: activar_ventana(boton, result_label))
    boton.grid(row=1, column=0, columnspan=2)
    root.mainloop()

if __name__ == '__main__':
    main()