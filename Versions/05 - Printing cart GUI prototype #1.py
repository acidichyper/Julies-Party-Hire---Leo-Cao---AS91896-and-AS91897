from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def Print_Cart():   #The cart menu GUI
    global main_window, frame_GUI, frame_output, frame_cart
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers

    #Resetting the cart frame GUI
    for widget in frame_cart.winfo_children():
        widget.destroy()
    frame_cart.pack_forget()

    #Printing the Labels and buttons
    frame_cart.grid(column = 0, row = 20, columnspan = 2, rowspan = 200, stick = W+N)
    Label(frame_cart, text = "                 ").grid(column = 0, row = 0)
    Label(frame_cart, text = "Current items in "+ entry_name.get()+"'s cart: ", font = "Courier 9 bold", fg = "midnight blue").grid(column = 0, row = 1, pady = 5, sticky = W, columnspan = 2)

    Cart_count = 0
    if total_cart_entries > 0:
        while Cart_count < total_cart_entries:
            Label(frame_cart, text = (Cart_list[Cart_count][0])).grid(column = 0, row = Cart_count+2)
            Label(frame_cart, text = ("x"+Cart_list[Cart_count][1])).grid(column = 1, row = Cart_count+2, sticky = W)
            Cart_count += 1

        Button(frame_cart, text = "Append Cart", command = Append_main, width = 14).grid(column = 0, row = Cart_count+3, sticky = E+W)
        Button(frame_cart, text = "Edit All Details", command = GUI_Delete, width = 19, state = "disabled").grid(column = 1, row = Cart_count+3, sticky = E+W, pady = 8)
