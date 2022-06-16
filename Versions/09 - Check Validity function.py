from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def check_validity():   #Checking if entry is valid
    global entry_name, Item, Combo_Items, Num, Combo_Num, Items
    global main_window, frame_GUI, frame_output, frame_cart
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries

    #Resetting the Labels colours
    Label(frame_GUI , text = "Customers Name: ").grid(column = 0, row = 1, sticky = E)
    Label(frame_GUI, text = "Items Hired: ").grid(column = 0, row = 2, sticky = E)
    Label(frame_GUI, text = "How much (item): ").grid(column = 0, row = 3, sticky = E)
    
    #Checking for appropriate inputs, and making sure input is filled
    if (entry_name.get()).strip() == "" or (entry_name.get()).strip().isdigit() or (Item.get()).strip() == "" or (Num.get()).strip() == "":
        if (entry_name.get()).strip() == "" or (entry_name.get()).strip().isdigit():
            Label(frame_GUI , text = "Customers Name: ", fg = "Red").grid(column = 0, row = 1, sticky = E)
        if (Item.get()).strip() == "":
            Label(frame_GUI, text = "Items Hired: ", fg = "Red").grid(column = 0, row = 2, sticky = E)
        if (Num.get()).strip() == "":
            Label(frame_GUI, text = "How much (item): ", fg = "Red").grid(column = 0, row = 3, sticky = E)
    else:
        Append_cart()   #if it is appropriate, append the cart
