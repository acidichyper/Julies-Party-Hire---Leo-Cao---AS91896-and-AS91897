from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

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
        Label(frame_output, text = (Final_list[name_count][0])).grid(column = 4, row = row_placement+2)
        Label(frame_output, text = (Final_list[name_count][1])).grid(column = 5, row = row_placement+2)
        total_items = len(Final_list[name_count][2])
        Item_count = 0
        while Item_count < total_items: #Printing out the items assigned to each customer
            Label(frame_output, text = (Final_list[name_count][2][Item_count][0])).grid(column = 6, row = row_placement+2)
            Label(frame_output, text = ("x"+Final_list[name_count][2][Item_count][1])).grid(column = 7, row = row_placement+2)
            row_placement += 1
            Item_count += 1
        row_placement += 1
        name_count += 1 
