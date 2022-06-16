from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def quit():     #Quit Funtion
    status = messagebox.askyesno(title="Warning Message!", message = "Are you sure you want to close out of the program?")
    if status == True:
        main_window.destroy()
    else:
        pass
