import tkinter as tk
import pygetwindow as gw
import pyautogui
import time

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

TITULO_BASE = "Ingreso de Datos"

index = 0
AUTOMATICO = False

def actions(result_label, indice):

    values = ",".join(str(value) for value in ROLLERS[indice].values())
    print(f"Index {indice}: {values}")
    result_label.config(text=f"Index {indice}: {values}")

    pyautogui.press('tab')
    pyautogui.write(values)
    pyautogui.press('enter')

def search_window(boton, result_label):
    """Busca la ventana y la activa"""

    ventana = None

    try:
        ventana = gw.getWindowsWithTitle(TITULO_BASE)[0]
    except IndexError:
        boton.config(state=tk.DISABLED)
        result_label.config(text="No se encontro la ventana")
        return False
    
    if ventana.isMinimized:
        ventana.restore()

    ventana.activate()
    return True


def activar_ventana(boton, result_label, auto = None):
    """Espera a que se abra la ventana y la activa"""

    if auto:
        global AUTOMATICO
        AUTOMATICO = auto

    global index

    def buscar_ventana():
        global index

        if not search_window(boton, result_label):
            return False

        boton.config(state=tk.NORMAL)
        
        if AUTOMATICO:
            for i in range(len(ROLLERS)):
                actions(result_label, i)
                if not search_window(boton, result_label):
                    return False
        else:
            actions(result_label, index)
        return True
    

    # while (auto != False) 
    # if index < len(ROLLERS):
    #     if search_window(boton, result_label):
    #         index += 1
    #     else:
    #         result_label.after(3000, activar_ventana, boton, result_label) 
    # else:
    #     boton.config(state=tk.DISABLED)            
    #     result_label.config(text="Terminado")


def automatic_mode(boton, result_label):
    """Automatic Mode"""

    global index

    while (index < len(ROLLERS)):
        if search_window(boton, result_label):
            boton.config(state=tk.NORMAL)
            actions(result_label, index)
            index += 1
        else:
            result_label.after(3000, automatic_mode, boton, result_label) 
            continue

    boton.config(state=tk.DISABLED)            
    result_label.config(text="Terminado")


def manual_mode(main_gui, boton, result_label):
    """Manual Mode"""
    index = main_gui.index_current
    print("HOLAAAA")
    boton.config(state=tk.DISABLED)

    while not search_window(boton, result_label):
        time.sleep(1)
        pass

    if index < len(ROLLERS):
        actions(result_label, index)
        main_gui.index_current += 1
        main_gui.update_index_label()
    else:
        result_label.config(text="Terminado")
    
    main_gui.master.after(2000,boton.config(state=tk.NORMAL))


    