"""
Este módulo proporciona una aplicación GUI simple utilizando tkinter para ingresar datos.

El usuario puede ingresar números separados por espacios, y la aplicación mostrará
los datos ingresados junto con un contador. La ventana se oculta temporalmente después
de cada entrada y se muestra nuevamente después de un breve retraso.
"""

import tkinter as tk

class Aplicacion:
    """
    Clase que representa una aplicación GUI simple para el ingreso de datos utilizando tkinter.

    Esta clase crea una ventana de interfaz gráfica que permite al usuario ingresar números 
    separados
    por espacios. Al presionar Enter, los datos ingresados se muestran junto con un contador, y la 
    ventana
    se oculta temporalmente antes de mostrarse nuevamente después de un breve retraso.

    Atributos:
    - contador: Contador de las veces que se ha ingresado un dato.
    - root: La ventana principal de la aplicación tkinter.
    - entrada: Campo de entrada de texto donde el usuario ingresa los datos.
    - resultado_var: StringVar utilizado para mostrar los resultados en una etiqueta.

    Métodos:
    - setup_ui(): Configura los elementos de la interfaz de usuario.
    - imprimir_datos(_event): Captura y muestra los datos ingresados y oculta la ventana 
    temporalmente.
    - mostrar_ventana(): Restablece el campo de entrada y muestra la ventana principal nuevamente.
    """
    def __init__(self, root):
        self.contador = 0
        self.root = root
        self.root.title("Ingreso de Datos")
        self.setup_ui()

    def setup_ui(self):
        """
        Configura la interfaz de usuario de la aplicación.

        Este método crea y organiza los elementos de la interfaz gráfica, incluyendo:
        - Una etiqueta con instrucciones para el usuario.
        - Un campo de entrada de texto donde el usuario puede ingresar números.
        - Una etiqueta que muestra los resultados después de que el usuario ingresa los datos.

        También asocia el evento de presionar Enter a la función de manejo de eventos 
        `imprimir_datos` para capturar la entrada del usuario.
        """
        etiqueta = tk.Label(self.root, text="Ingresa los números separados por espacios:")
        etiqueta.pack(pady=10)

        self.entrada = tk.Entry(self.root, width=30)
        self.entrada.pack(pady=10)
        self.entrada.bind('<Return>', self.imprimir_datos)

        self.resultado_var = tk.StringVar()
        etiqueta_resultado = tk.Label(self.root, textvariable=self.resultado_var)
        etiqueta_resultado.pack(pady=10)

    def imprimir_datos(self, _event):
        """
        Maneja el evento de presionar Enter para capturar datos ingresados,
        mostrar un mensaje y ocultar la ventana por 3 segundos.

        Argumentos:
        _event -- Parámetro necesario para el evento de tkinter, pero no utilizado.
        """
        datos_ingresados = self.entrada.get()
        print(datos_ingresados)
        print("Contador:", self.contador)

        self.resultado_var.set(f"Datos ingresados: {datos_ingresados}")

        self.root.withdraw()

        self.contador += 1
        self.root.after(3000, self.mostrar_ventana)

    def mostrar_ventana(self):
        """
        Restablece la entrada de texto y muestra la ventana principal de la aplicación.

        Este método limpia el campo de entrada, restablece el texto de la etiqueta de resultados
        y vuelve a mostrar la ventana principal después de que se haya ocultado. Es útil para
        proporcionar una retroalimentación visual al usuario y permitir la entrada de nuevos datos.
        """
        self.entrada.delete(0, tk.END)
        self.resultado_var.set("")
        self.root.deiconify()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
