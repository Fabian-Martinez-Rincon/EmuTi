import tkinter as tk
import json
import pygetwindow as gw
import pyautogui
import os

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

PATH_PROSSED = "C:/Users/Fabian/Desktop/Fortuna.xlsx"

SEM_ACTION = False

def activar_ventana(boton):
    """Espera a que se abra la ventana y la activa"""
    while True:
        try:
            ventana = gw.getWindowsWithTitle(TITULO_BASE)[0]            
            ventana.activate()
            boton.config(state=tk.NORMAL)
            return ventana
        except IndexError:
            pyautogui.sleep(1)

def mostrar_registro(datos, boton):
    global SEM_ACTION
    os.system('cls')

    global INDICE
    registro = datos[INDICE]
    valores = [
        registro[campo]
        for campo in CAMPOS
        ]

    r_valores_text = ", ".join(str(valores[i]) for i, campo in enumerate(CAMPOS) if campo.startswith('R'))
    simbolo_valores_text = ", ".join(str(valores[i]) for i, campo in enumerate(CAMPOS) if campo.startswith('SIMBOLO'))

    print('Datos Confirmados:')
    print('INDICE: ' + str(INDICE))
    print(r_valores_text)
    print(simbolo_valores_text)
    
    ventana = activar_ventana(boton)
    pyautogui.write(str(r_valores_text))
    pyautogui.press('enter')
    
    INDICE += 1
    boton.config(state=tk.DISABLED)

def click_boton(datos, boton):

    
    boton.config(state=tk.DISABLED)
    activar_ventana(boton)

    if INDICE < len(datos):
        mostrar_registro(datos, boton)
    else:
        print("Todos los datos han sido procesados.")

def main():
    root = tk.Tk()
    boton = tk.Button(root, text='Siguiente', command=lambda: click_boton(DATA, boton))
    boton.grid(row=1, column=0, columnspan=2)
    root.mainloop()

if __name__ == '__main__':
    main()