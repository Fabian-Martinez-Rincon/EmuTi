"""
Este módulo define los colores y estilos para la interfaz gráfica 
de usuario (GUI) utilizando tkinter.

Contiene constantes para los colores de fondo, el color de letra, 
y estilos de fuentes utilizados en alertas y títulos. También incluye 
funciones para generar ventanas emergentes de alerta para errores, 
éxitos, y excepciones.

Constantes:
    BACKGROUND_COLOR_ERROR (str): Color de fondo para alertas de error.
    BACKGROUND_COLOR_SUCCESS (str): Color de fondo para alertas de éxito.
    BACKGROUND_COLOR_EXCEPT (str): Color de fondo para alertas de excepción.
    LETTER (str): Color de la letra usado en las alertas.
    FUENTE (tuple): Fuente estándar usada en las alertas.

Este módulo requiere `tkinter` para manejar la interfaz gráfica.
"""

import tkinter as tk

BACKGROUND_COLOR_ERROR = "#2f2d2d"
BACKGROUND_COLOR_SUCCESS = "#699fd0"
BACKGROUND_COLOR_EXCEPT = "#800000"
LETTER = "#FFFFFF"
FUENTE = ("Bolt", 12)

STYLE_ERROR = {
  "font": FUENTE, 
  "foreground": LETTER, 
  "background": BACKGROUND_COLOR_ERROR
}

STYLE_SUCCESS = {
  "font": FUENTE, 
  "foreground": LETTER, 
  "background": BACKGROUND_COLOR_SUCCESS
}

STYLE_EXCEPT = {
  "font": FUENTE, 
  "foreground": LETTER, 
  "background": BACKGROUND_COLOR_EXCEPT
}


STYLE_TITLE = {
  "font": ("Helvetica", 10, "bold"), 
  "bg":"#add8e6"
}

def alert_error(window , message, timer=2000):
    """
    Muestra una ventana emergente de error con un mensaje específico.

    Args:
        window (tk.Tk): Ventana principal de tkinter.
        message (str): Mensaje de error a mostrar.
        timer (int, opcional): Duración en milisegundos antes de cerrar la ventana.
        Por defecto es 2000 ms.
    """
    popup = tk.Toplevel(window)
    popup.title("ERROR")
    popup.geometry("300x50")

    popup.configure(bg=BACKGROUND_COLOR_ERROR)

    label = tk.Label(popup, text=message, **STYLE_ERROR)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)

def alert_success(window , message, timer=2000):
    """
    Muestra una ventana emergente de éxito con un mensaje específico.

    Args:
        window (tk.Tk): Ventana principal de tkinter.
        message (str): Mensaje de éxito a mostrar.
        timer (int, opcional): Duración en milisegundos antes de cerrar la ventana.
        Por defecto es 2000 ms.
    """
    popup = tk.Toplevel(window)
    popup.title("CAMBIO DE ESTADO")
    popup.geometry("300x50")

    popup.configure(bg=BACKGROUND_COLOR_SUCCESS)

    label = tk.Label(popup, text=message, **STYLE_SUCCESS)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)

def alert_except(window , message, timer=2000):
    """
    Muestra una ventana emergente de excepción con un mensaje específico.

    La ventana cambia de tamaño según la longitud del mensaje.

    Args:
        window (tk.Tk): Ventana principal de tkinter.
        message (str): Mensaje de excepción a mostrar.
        timer (int, opcional): Duración en milisegundos antes de cerrar la ventana.
        Por defecto es 2000 ms.
    """
    popup = tk.Toplevel(window)
    popup.title("EXCEPTION")
    if len(message) <= 20:
        popup.geometry("300x50")
    elif len(message) <= 60:
        popup.geometry("350x50")
    else:
        popup.geometry("800x50")

    popup.configure(bg=BACKGROUND_COLOR_EXCEPT)
    label = tk.Label(popup, text=message, **STYLE_EXCEPT)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)

PADY=10
PADX=10
COLUMNSPAN=2

def title_style(master, message, x, y):
    """
    Aplica estilo al título de la ventana o sección.

    Args:
        master (tk.Tk): Ventana o marco de tkinter.
        message (str): Texto del título.
        x (int): Fila en la cuadrícula donde se colocará el título.
        y (int): Columna en la cuadrícula donde se colocará el título.
    """
    master.auto_title_label = tk.Label(master, text=message, **STYLE_TITLE)
    master.auto_title_label.grid(row=x, column=y, pady=PADY, padx=PADX, columnspan=COLUMNSPAN)
