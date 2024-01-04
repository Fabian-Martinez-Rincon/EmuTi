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
    popup = tk.Toplevel(window)
    popup.title("ERROR")
    popup.geometry("300x50")

    popup.configure(bg=BACKGROUND_COLOR_ERROR)
    
    label = tk.Label(popup, text=message, **STYLE_ERROR)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)

def alert_success(window , message, timer=2000):
    popup = tk.Toplevel(window)
    popup.title("CAMBIO DE ESTADO")
    popup.geometry("300x50")

    popup.configure(bg=BACKGROUND_COLOR_EXCEPT)
    
    label = tk.Label(popup, text=message, **STYLE_EXCEPT)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)
    
def alert_except(window , message, timer=5000):
    popup = tk.Toplevel(window)
    popup.title("EXCEPTION")
    popup.geometry("300x50")

    popup.configure(bg=BACKGROUND_COLOR_SUCCESS)
    
    label = tk.Label(popup, text=message, **STYLE_SUCCESS)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)

PADY=10
PADX=10
COLUMNSPAN=2

def title_style(master, message, x, y):
    master.auto_title_label = tk.Label(master, text=message, **STYLE_TITLE)
    master.auto_title_label.grid(row=x, column=y, pady=PADY, padx=PADX, columnspan=COLUMNSPAN)