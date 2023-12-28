import tkinter as tk

def mostrar_popup():
    popup = tk.Toplevel()
    popup.title("Pop-up Personalizado")

    label = tk.Label(popup, text="¡Hola! Soy un pop-up personalizado.")
    label.pack(padx=20, pady=20)

    btn_cerrar = tk.Button(popup, text="Cerrar", command=popup.destroy)
    btn_cerrar.pack(pady=10)

def crear_ventana_principal():
    root = tk.Tk()
    root.title("Ventana Principal")

    btn_mostrar_popup = tk.Button(root, text="Mostrar Pop-up", command=mostrar_popup)
    btn_mostrar_popup.pack(pady=20)

    root.mainloop()

crear_ventana_principal()
