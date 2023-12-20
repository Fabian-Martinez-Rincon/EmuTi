from tkinter import *
from tkinter import messagebox

Calculator = Tk()
Calculator.title("AdictoCalculator")
Calculator.resizable(False, False)
Calculator.config(cursor="pencil")
root = Pycalc(Calculator).grid()
Calculator.mainloop()