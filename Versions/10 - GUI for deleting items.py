from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def GUI_Delete():   #Deleting Entries GUI
    global Delete_All_Button, Back_Button, Combo_Receipt, receipts
    global main_window, frame_GUI, frame_output, frame_cart
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers

    #Deleting the old main GUI
    for widget in frame_GUI.winfo_children():
        widget.destroy()
    frame_GUI.pack_forget()

    for widget in frame_cart.winfo_children():
        widget.destroy()
    frame_cart.pack_forget()

    #Creating a new frame
    frame_GUI.grid(column = 0, row = 0, columnspan = 2, rowspan = 2, stick = N+W)
    
    #Title/buttons
    Label(frame_GUI, text = "Julies Party Hire Store", font = "Courier 12").grid(column = 0, row = 0, pady = 11, columnspan = 2)

    #Receipt input
    Label(frame_GUI , text = "Recipt #:", width = 14).grid(column = 0, row = 1, sticky = E)
    receipts = StringVar()        # StringVar is my function
    Combo_Receipt = ttk.Combobox(frame_GUI, textvariable = receipts, value = Recipt_Numbers, state = "readonly")
    Combo_Receipt.grid(row = 1, column = 1,sticky = E+W)
    Combo_Receipt.bind('<<ComboboxSelected>>', on_select) #Bind funtion to check wether or not the combobox is updated
    
    #Buttons
    Back_Button = Button(frame_GUI, text = "Back", command = GUI_append, width = 14)
    Back_Button.grid(column = 0, row = 2, sticky = E+W)
    Delete_All_Button = Button(frame_GUI, text = "Delete all?", width = 19, state = "disabled")
    Delete_All_Button.grid(column = 1, row = 2, sticky = E+W, pady = 10)
