from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def on_select(event):   #Funtion runs when combobox is updated
    global Delete_All_Button, Back_Button, Combo_Receipt
    global main_window, frame_GUI, frame_output, frame_cart
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers

    try:    #Try function to check if an error will accour
        selected = event.widget.get()   #get the variable from the event
    except:
        selected = Combo_Receipt.get()  #else if error, get variable from the combobox
        
    #Cleaning up the GUI
    Delete_All_Button.destroy()
    Back_Button.destroy()

    #Reseting the frame
    for widget in frame_cart.winfo_children():
        widget.destroy()
    frame_cart.pack_forget()

    frame_cart.grid(column = 0, row = 2, columnspan = 2, rowspan = 200, sticky = N+W)
    
    #Updating the new information
    for i in range (len(Final_list)):
        #Checking which customer matches with the receipt
        if Final_list[i][1] == selected:
            Label(frame_cart, text = "").grid(column = 0, row = 2, sticky = W, columnspan = 2)
            Label(frame_cart, text = "Current items in "+Final_list[i][0]+"'s cart: ", fg = "midnight blue").grid(column = 0, row = 3, pady = 5, sticky = W, columnspan = 2)
            Item_count = 0
            total_items = len(Final_list[i][2])
            #Print out all the customers cart and orders
            while Item_count < total_items:
                Label(frame_cart, text = (Final_list[i][2][Item_count][0])).grid(column = 0, row = Item_count+4)
                #Using clones of buttons, the lambda funtion will create a button with different variable assigned to each item
                Button(frame_cart,  text="Delete Item", command = lambda s=Item_count: Delete_Item(s)).grid(column = 1, row = Item_count+4, sticky = E+W)
                Item_count += 1
            #Matching the buttons with the new GUI
            Button(frame_cart, text = "Back", command = GUI_append, width = 14).grid(column = 0, row = Item_count+4, sticky = E+W)
            Button(frame_cart, text = "Delete all?", width = 19, command = delete_all, fg = "red").grid(column = 1, row = Item_count+4, sticky = E+W, pady = 8)
