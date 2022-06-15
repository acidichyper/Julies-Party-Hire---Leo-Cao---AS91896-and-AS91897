from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def GUI_append():   #Main GUI's - Main screen
    global main_window, frame_GUI, frame_output, frame_cart
    global entry_name, Item, Combo_Items, Num, Combo_Num, Items

    #Removing the previous Frame
    for widget in frame_GUI.winfo_children():
        widget.destroy()
    frame_GUI.pack_forget()
    
    for widget in frame_cart.winfo_children():
        widget.destroy()
    frame_cart.pack_forget()

    #Reseting the frame
    frame_GUI.grid(column = 0, row = 0, columnspan = 2, rowspan = 20, stick = N+W)
    
    #Title/buttons
    Label(frame_GUI, text = "Julies Party Hire Store", font = "Courier 12").grid(column = 0, row = 0, pady = 11, columnspan = 2)
    Button(frame_GUI, text = "QUIT", width = 14, fg = "Red").grid(column = 0, row = 4, sticky = E+W)
    Button(frame_GUI, text = "Add to cart", width = 19).grid(column = 1, row = 4, sticky = E+W)

    #Customers name
    Label(frame_GUI , text = "Customers Name: ").grid(column = 0, row = 1, sticky = E)
    entry_name = Entry(frame_GUI)
    entry_name.grid(column = 1, row = 1, sticky = E+W)

    #Items hired
    Label(frame_GUI, text = "Items Hired: ").grid(column = 0, row = 2, sticky = E)
    Items = ['Chairs', 'Foldable Tables', 'Decoration', 'Silverware', 'Balloons', 'Plates',
             'Linen', 'Party Games', 'Catering', 'Props', 'Lighting', 'Backdrops']
    Item = StringVar()        # StringVar is my function
    Combo_Items = ttk.Combobox(frame_GUI, textvariable = Item, value = Items, state = "readonly").grid(row = 2, column = 1,sticky = E+W)

    #How much Items
    Label(frame_GUI, text = "How much (item): ").grid(column = 0, row = 3, sticky = E)
    Num = StringVar()        # StringVar is my function
    Combo_Num = ttk.Spinbox(frame_GUI, textvariable = Num, from_= 1, to = 500, state = "readonly").grid(row = 3, column = 1, sticky = E+W)



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
