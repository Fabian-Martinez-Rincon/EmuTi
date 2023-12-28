import tkinter as tk
from tkinter import messagebox

def show_warning():
    messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")

# Crear la ventana principal
app = tk.Tk()
app.title("Ejemplo de Pop-up")

# Crear un botón que muestra la advertencia
warning_button = tk.Button(app, text="Mostrar Advertencia", command=show_warning)
warning_button.pack(pady=20)

# Ejecutar la aplicación
app.mainloop()
