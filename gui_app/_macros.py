import tkinter as tk

BACKGROUND_COLOR_ERROR = "#2f2d2d"

BACKGROUND_COLOR_SUCCESS = "##699fd0"

STYLE_ERROR = {
  "font": ("Bolt", 12), 
  "foreground": "#FFFFFF", 
  "background": BACKGROUND_COLOR_ERROR
}

def alert_error(window , message, timer=2000):
    popup = tk.Toplevel(window)
    popup.title("ERROR")
    popup.geometry("300x50")

    popup.configure(bg=BACKGROUND_COLOR_ERROR)
    
    label = tk.Label(popup, text=message, **STYLE_ERROR)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)


BACKGROUND_COLOR_SUCCESS = "#699fd0"

STYLE_SUCCESS = {
  "font": ("Bolt", 12), 
  "foreground": "#FFFFFF", 
  "background": BACKGROUND_COLOR_SUCCESS
}


def alert_success(window , message, timer=2000):
    popup = tk.Toplevel(window)
    popup.title("CAMBIO DE ESTADO")
    popup.geometry("300x50")

    popup.configure(bg=BACKGROUND_COLOR_SUCCESS)
    
    label = tk.Label(popup, text=message, **STYLE_SUCCESS)
    label.pack(pady=10)

    popup.after(timer, popup.destroy)