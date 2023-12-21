import tkinter as tk
import json
import pygetwindow as gw
import pyautogui
import os

TITULO_BASE = input("Por favor, ingrese una cadena: ")
INDICE = int(input("Elemento a comenzar 0..10 por ejemplo: "))

CAMPOS = [
    'SIMBOLO', 'SIMBOLO.1', 'SIMBOLO.2', 'SIMBOLO.3', 'SIMBOLO.4', 'R1', 'R2', 'R3', 'R4', 'R5'
    ]

PATH_BASE = os.path.dirname(os.path.abspath(__file__))
PATH_SOURCE = os.path.join(PATH_BASE, "processed_json")
PATH_PROSSED = os.path.join(PATH_SOURCE, "Freegames.json")

def activar_ventana():
    """Espera a que se abra la ventana y la activa"""
    while True:
        ventana = gw.getWindowsWithTitle(TITULO_BASE)
        if ventana:
            return ventana[0]
        else:
            print("La ventana no está abierta. Esperando...")
            pyautogui.sleep(1)

def mostrar_registro(datos, boton):
    os.system('cls')

    global INDICE
    registro = datos[INDICE]
    valores = [
        registro[campo]
        for campo in CAMPOS
        ]

    r_valores_text = ", ".join([
        str(valores[i]) 
        for i, campo in enumerate(CAMPOS) 
        if campo.startswith('R')
    ])

    simbolo_valores_text = ", ".join([
        str(valores[i]) 
        for i, campo in enumerate(CAMPOS)
        if campo.startswith('SIMBOLO')
    ])

    print('Datos Confirmados:')
    print('INDICE: ' + str(INDICE))
    print(r_valores_text)
    print(simbolo_valores_text)
    
    ventana = activar_ventana()
    ventana.activate()
    pyautogui.write(str(r_valores_text))
    pyautogui.press('enter')
    
    INDICE += 1
    if INDICE >= len(datos):
        boton.config(state=tk.DISABLED)

def click_boton(datos, boton):
    mostrar_registro(datos, boton)
    boton.config(state=tk.DISABLED)
    boton.after(1500, lambda: boton.config(state=tk.NORMAL))

def main():
    with open(PATH_PROSSED, 'r') as archivo:
        datos = json.load(archivo)

    root = tk.Tk()
    boton = tk.Button(root, text='Siguiente', command=lambda: click_boton(datos, boton))
    boton.grid(row=1, column=0, columnspan=2)
    root.mainloop()

if __name__ == '__main__':
    main()