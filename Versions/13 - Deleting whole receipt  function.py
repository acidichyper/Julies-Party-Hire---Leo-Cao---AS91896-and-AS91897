from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def delete_all():   #Deleting everything from the customer
    global main_window, frame_GUI, frame_output, frame_cart, Combo_Receipt, receipts
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers

    for i in range(len(Final_list)):   
        if Final_list[i][1] == Combo_Receipt.get():#Checking which customer matches with the receipt
            Final_list.pop(i)   #popping the customer from the main list
            Recipt_Numbers.pop(i)   #popping the receipt number from the combobox 
            receipts.set("")    #Making the entry blank
            total_entries -= 1  #Removing one less entry from the list

            break #Breaking the list, in order for the program to not get an index error

    #Resseting the frames and GUI
    for widget in frame_output.winfo_children():
        widget.destroy()
    frame_output.pack_forget()

    print_main()
    GUI_Delete()
