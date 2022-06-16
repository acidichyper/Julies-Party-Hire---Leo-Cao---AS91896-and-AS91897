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

def Delete_Item(item_id):   #Deleting seperate items from a list
    global main_window, frame_GUI, frame_output, frame_cart, Combo_Receipt
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers
    
    for i in range(len(Final_list)):
        if Final_list[i][1] == Combo_Receipt.get(): #Checking which customer matches with the receipt
            if len(Final_list[i][2]) == 1:  #Checking if this would remove the customer
                delete_all()    #If it does, then run the delete all function instead
                break    #Breaking the list, in order for the program to not get an index error
            else:
                Final_list[i][2].pop(item_id)   #popping the individual item from thier cart list
                
                #Resetting all the GUI
                for widget in frame_output.winfo_children():
                    widget.destroy()
                frame_output.pack_forget()

                on_select(Combo_Receipt.get)
                print_main()

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

def print_main():   #Printing Details
    global main_window, frame_GUI, frame_output, frame_cart
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers

    #Printing the Labels in the frame
    Label(frame_output, text = "         ").grid(column = 3, row = 0)
    Label(frame_output, text = "Customer Name ", font = "Courier 9 bold").grid(column = 4, row = 0, padx = 15, pady = 11)
    Label(frame_output, text = "Recipt # ", font = "Courier 9 bold").grid(column = 5, row = 0, padx = 15)
    Label(frame_output, text = "Items Hired ", font = "Courier 9 bold").grid(column = 6, row = 0, padx = 15)
    Label(frame_output, text = "Item Count ", font = "Courier 9 bold").grid(column = 7, row = 0, padx = 15)
    frame_output.grid(column = 3, row = 0, columnspan = 5, rowspan = 600, stick = N)

    #Printing all the entries in order
    name_count = 0
    row_placement = 0
    while name_count < total_entries:   #Printing out all the names and receipt numbers
        Label(frame_output, text = "---"*30).grid(column = 4, row = row_placement+1, columnspan = 4)
        Label(frame_output, text = (Final_list[name_count][0])).grid(column = 4, row = row_placement+2)
        Label(frame_output, text = (Final_list[name_count][1]), fg = "dark green").grid(column = 5, row = row_placement+2)
        total_items = len(Final_list[name_count][2])
        Item_count = 0
        while Item_count < total_items: #Printing out the items assigned to each customer
            Label(frame_output, text = (Final_list[name_count][2][Item_count][0])).grid(column = 6, row = row_placement+2)
            Label(frame_output, text = ("x"+Final_list[name_count][2][Item_count][1])).grid(column = 7, row = row_placement+2)
            row_placement += 1
            Item_count += 1
        row_placement += 1
        name_count += 1 

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

def Append_cart():  #Appending the entries to the cart
    global entry_name, Item, Combo_Items, Num, Combo_Num, Items
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers

    #appending and disabling the entry
    entry_name["state"] = "disabled"
    Cart_list.append([Item.get(), Num.get()])
    total_cart_entries += 1

    #Removing the item from the list
    for i in range (len(Items)):
        if Items[i] == Item.get():
            Items.pop(i)
            break
    Combo_Items = ttk.Combobox(frame_GUI, textvariable = Item, value = Items, state = "readonly").grid(row = 2, column = 1,sticky = E+W)

    #setting the entries as blank
    Item.set("")
    Num.set("")

    Print_Cart()

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

    Print_Cart_Final()

def Print_Cart_Final():     #Printing the cart detials
    global main_window, frame_GUI, frame_output, frame_cart, frame_delete
    global Cart_list, Receipt_list, Final_list, total_entries, total_cart_entries, Recipt_Numbers
    Cart_count = 0
    if total_cart_entries > 0:
        while Cart_count < total_cart_entries:
            Label(frame_cart, text = (Cart_list[Cart_count][0])).grid(column = 0, row = Cart_count+2)
            Label(frame_cart, text = ("x"+Cart_list[Cart_count][1])).grid(column = 1, row = Cart_count+2, sticky = W)
            Cart_count += 1

        Button(frame_cart, text = "Append Cart", command = Append_main, width = 14).grid(column = 0, row = Cart_count+3, sticky = E+W)
        Button(frame_cart, text = "Edit All Details", command = GUI_Delete, width = 19, state = "disabled").grid(column = 1, row = Cart_count+3, sticky = E+W, pady = 8)
    else:
        frame_cart.grid(column = 0, row = 20, columnspan = 2, rowspan = 200, stick = W+N)
        Button(frame_cart, text = "Append Cart", width = 14, state = "disabled").grid(column = 0, row = 1, sticky = E+W)
        Button(frame_cart, text = "Edit All Details", command = GUI_Delete, width = 19).grid(column = 1, row = 1, sticky = E+W, pady = 8)


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
    Button(frame_GUI, text = "QUIT", command = quit, width = 14, fg = "Red").grid(column = 0, row = 4, sticky = E+W)
    Button(frame_GUI, text = "Add to cart", command = check_validity, width = 19).grid(column = 1, row = 4, sticky = E+W)

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

    print_main()
    Print_Cart_Final()


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
