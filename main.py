"""
Este módulo inicializa y ejecuta la aplicación GUI principal utilizando tkinter.

La aplicación utiliza la clase MainGUI, importada desde el módulo `gui_app.main_gui`,
para definir la interfaz gráfica y su funcionalidad.
"""

import tkinter as tk
from gui_app.main_gui import MainGUI

def main():
    """
    Configura y ejecuta la ventana principal de la aplicación GUI.

    Esta función crea una instancia de tkinter `Tk`, establece el título de la ventana,
    deshabilita el cambio de tamaño, crea una instancia de la clase `MainGUI` y configura
    el color de fondo. Finalmente, inicia el bucle principal de la GUI.

    Returns:
        None
    """
    app = tk.Tk()
    app.title("Emuti")
    app.resizable(False, False)

    gui_instance = MainGUI(master=app)
    gui_instance.configure(bg="#add8e6")
    gui_instance.mainloop()

if __name__ == "__main__":
    main()
