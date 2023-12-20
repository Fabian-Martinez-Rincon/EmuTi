import tkinter as tk
from tkinter import filedialog

class MyApp(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.grid()
        self.create_widgets()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            self.file_label.config(text="Archivo seleccionado: {}".format(file_path))
            self.print_file_content(file_path)

    def print_file_content(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print("Contenido del archivo:")
                print(content)
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    def show_window_value(self):
        window_value = self.window_entry.get()
        print(f"Valor de la ventana: {window_value}")

    def show_numeric_value(self):
        numeric_value = self.value_entry.get()
        print(f"Valor numérico: {numeric_value}")

    def automatic_operation(self):
        # Lógica para la operación automática
        self.toggle_automatic()

    def toggle_automatic(self):
        current_state = self.auto_var.get()
        new_state = not current_state
        self.auto_var.set(new_state)
        self.update_auto_button()

    def update_auto_button(self):
        if self.auto_var.get():
            self.auto_on_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
            self.auto_off_button.grid_remove()
        else:
            self.auto_on_button.grid_remove()
            self.auto_off_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    def next_step(self):
        # Lógica para avanzar al siguiente paso
        self.result_label.config(text="Siguiente paso")

    def create_widgets(self):
        self.file_button = tk.Button(self, text="Seleccionar Archivo", command=self.open_file_dialog)
        self.file_button.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        self.file_label = tk.Label(self, text="")
        self.file_label.grid(row=1, column=0, pady=10, padx=10, columnspan=2)

        self.auto_var = tk.BooleanVar()

        self.auto_on_button = tk.Button(self, text="Automático ON", command=self.automatic_operation)
        self.auto_on_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

        self.auto_off_button = tk.Button(self, text="Automático OFF", command=self.toggle_automatic)
        self.auto_off_button.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
        self.auto_off_button.grid_remove()

        self.next_button = tk.Button(self, text="Siguiente", command=self.next_step)
        self.next_button.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

        self.window_label = tk.Label(self, text="Nombre de la ventana:")
        self.window_label.grid(row=4, column=0, pady=10, padx=10)

        self.window_entry = tk.Entry(self)
        self.window_entry.grid(row=5, column=0, pady=10, padx=10)

        self.show_window_button = tk.Button(self, text="Mostrar Valor", command=self.show_window_value)
        self.show_window_button.grid(row=5, column=1, pady=10, padx=10)

        self.value_label = tk.Label(self, text="Valor numérico:")
        self.value_label.grid(row=6, column=0, pady=10, padx=10)

        self.value_entry = tk.Entry(self)
        self.value_entry.grid(row=7, column=0, pady=10, padx=10)

        self.show_numeric_button = tk.Button(self, text="Mostrar Valor", command=self.show_numeric_value)
        self.show_numeric_button.grid(row=7, column=1, pady=10, padx=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=8, column=0, pady=10, padx=10, columnspan=2)

app = tk.Tk()
app.title("Emuti")
app.resizable(False, False)

my_app = MyApp(master=app)
my_app.mainloop()
