from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def Append_main():  #Appending the cart details to the main list
    global entry_name, Item, Combo_Items, Num, Combo_Num, Items
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers
    
    #Resseting all the GUI
    for widget in frame_cart.winfo_children():
        widget.destroy()
    frame_cart.pack_forget()

    #Appending Items
    receipt = "#"+str(random.randint(10000,99999))
    Final_list.append([entry_name.get(), receipt, Cart_list])
    Recipt_Numbers.append(receipt)

    #Updating the Variables
    total_entries += 1
    total_cart_entries = 0
    Cart_list = []

    GUI_append()
    print_main()
