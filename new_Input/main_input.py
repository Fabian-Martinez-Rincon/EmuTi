import tkinter as tk
import pygetwindow as gw
import pyautogui


import tkinter as tk
import json
import pygetwindow as gw
import pyautogui
import os

INDICE = 0
DATA = [
    {"SIMBOLO": "W", "SIMBOLO.1": "W", "SIMBOLO.2": "W", "SIMBOLO.3": "W", "SIMBOLO.4": "W", "R1": 3, "R2": 6, "R3": 8, "R4": 32, "R5": 5},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "F", "SIMBOLO.4": "F", "R1": 4, "R2": 11, "R3": 23, "R4": 5, "R5": 12},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "F", "SIMBOLO.4": "W", "R1": 4, "R2": 11, "R3": 23, "R4": 5, "R5": 5},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "W", "SIMBOLO.4": "F", "R1": 4, "R2": 11, "R3": 23, "R4": 32, "R5": 12},
    {"SIMBOLO": "F", "SIMBOLO.1": "F", "SIMBOLO.2": "F", "SIMBOLO.3": "W", "SIMBOLO.4": "W", "R1": 4, "R2": 11, "R3": 23, "R4": 32, "R5": 5}
]
CAMPOS = ['SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5']
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