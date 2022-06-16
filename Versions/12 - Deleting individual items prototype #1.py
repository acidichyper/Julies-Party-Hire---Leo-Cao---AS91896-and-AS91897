from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def Delete_Item(item_id):   #Deleting seperate items from a list
    global main_window, frame_GUI, frame_output, frame_cart, Combo_Receipt
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers
    
    for i in range(len(Final_list)):
        if Final_list[i][1] == Combo_Receipt.get(): #Checking which customer matches with the receipt
            Final_list[i][2].pop(item_id)   #popping the individual item from thier cart list
            
            #Resetting all the GUI
            for widget in frame_output.winfo_children():
                widget.destroy()
            frame_output.pack_forget()

            on_select(Combo_Receipt.get)
            print_main()
