import tkinter as tk

def imprimir_datos(event):
    datos_ingresados = entrada.get()
    print(datos_ingresados)
    etiqueta_resultado.config(text="Datos ingresados: " + datos_ingresados)
    ventana.withdraw()

    ventana.after(2000, mostrar_ventana)

def mostrar_ventana():
    ventana.deiconify()  
    etiqueta_resultado.config(text="") 
    entrada.delete(0, tk.END) 
    entrada.focus_set()

ventana = tk.Tk()
ventana.title("Ingreso de Datos")

etiqueta = tk.Label(ventana, text="Ingresa los números separados por espacios:")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)
entrada.focus_set()

entrada.bind('<Return>', imprimir_datos)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
