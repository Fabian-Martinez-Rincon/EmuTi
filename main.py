from gui_app.main_gui import MainGUI
import tkinter as tk

def main():
    app = tk.Tk()
    app.title("Emuti")
    app.resizable(False, False)

    gui_instance = MainGUI(master=app)
    gui_instance.configure(bg="#add8e6")
    gui_instance.mainloop()

if __name__ == "__main__":
    main()