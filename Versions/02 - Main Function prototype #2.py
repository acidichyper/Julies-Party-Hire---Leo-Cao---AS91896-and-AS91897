from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def main():     #Main function for all variables
    global main_window, frame_GUI, frame_output, frame_cart
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers
    
    #Lists and variables
    Cart_list = []
    Receipt_list = []
    Final_list = []
    Recipt_Numbers = []
    total_entries = 0
    total_cart_entries = 0

    #Tkinter Window and Frames
    main_window = Tk()
    main_window.title("Julies Party Hire Assessment - Leo Cao")
    main_window.geometry("800x550+200+50")

    frame_GUI = Frame(main_window)
    frame_output = Frame(main_window)
    frame_cart = Frame(main_window)
    GUI_append()

    main_window.mainloop()
    

main()
