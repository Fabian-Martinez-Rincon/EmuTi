import tkinter as tk

def on_button_click():
    button.config(state=tk.DISABLED)  # Deshabilita el botón al hacer clic
    # Realiza tus acciones aquí
    # Simula una acción que lleva tiempo
    print("Haciendo clic en el botón")
    root.after(2000, enable_button)  # Vuelve a habilitar el botón después de 2000 milisegundos (2 segundos)

def enable_button():
    button.config(state=tk.NORMAL)  # Vuelve a habilitar el botón

root = tk.Tk()

button = tk.Button(root, text="Haz clic", command=on_button_click)
button.pack(pady=10)

root.mainloop()