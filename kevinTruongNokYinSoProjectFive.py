# Project 5: Pizza Project
# 12/9/2024
# Kevin Truong, Nok Yin So
# This program simulates ordering a pizza.

from tkinter import *

# Tax rate
TAX = 0.0875

# Calculates the cost and prints the receipt of an ordered pizza 
def click():
    # Prints the thank-you message on the receipt 
    receipt.insert(END, "Thank you for choosing K&L's Pizzeria!\n\n")
    # Prints the name on the receipt    
    name = nameEntry.get()
    receipt.insert(END, "Order Name: \n" + name + "\n")
    price = 0
    
    # Prints the pizza size on the receipt
    receipt.insert(END, "Pizza Size: \n")
    match selectedSize.get():
        case "Small ($10.99)":
            receipt.insert(END, "Small")
            price += 10.99
        case "Medium ($12.99)":
            receipt.insert(END, "Medium")
            price += 12.99
        case "Large ($14.99)":
            receipt.insert(END, "Large")
            price += 14.99
        case _:
            receipt.insert(END, "No size entered!")
    receipt.insert(END, "\n")
        
    # Prints the crust type on the receipt
    receipt.insert(END, "Crust Type: \n")
    match selectedCrust.get():
        case 1:
            receipt.insert(END, "Hand-Tossed")
        case 2:
            receipt.insert(END, "Deep-Dish")
        case 3:
            receipt.insert(END, "Thin-Crust")
        case _:
            receipt.insert(END, "No crust type entered!")
    receipt.insert(END, "\n")
    
    # Prints the selected toppings on the receipt
    toppingsList = []
    toppingsList.append("Cheese")
    if pepperoniSelection.get() == 1:
        toppingsList.append("Pepperoni")
    if sausageSelection.get() == 1:
        toppingsList.append("Sausages")
    if mushroomSelection.get() == 1:
        toppingsList.append("Mushrooms")
    if onionSelection.get() == 1:
        toppingsList.append("Onions")
    receipt.insert(END, "Toppings: \n")
    if len(toppingsList) > 0:
        for i in range(len(toppingsList)):
            receipt.insert(END, toppingsList[i])
            if i < len(toppingsList) - 1:
                receipt.insert(END, ", ")
    else:
        receipt.insert(END, "Cheese")
    receipt.insert(END, "\n")        
    # Adds the additional cost of toppings to the price
    price += (len(toppingsList) - 1) * 1.25
    
    # Prints the initial price, tax, and price after tax on the receipt
    receipt.insert(END, "Subtotal: $%.2f" % price + "\n")
    taxAddition = price * TAX
    receipt.insert(END, "Tax: $%.2f" % taxAddition + "\n")
    price += taxAddition
    receipt.insert(END, "Total: $%.2f" % price + "\n")
            
    

# Creates the window with the given name
window = Tk()
window.title("Kevin and Lawrence's Pizzeria")
window.geometry("800x1000")
window.configure(background="navajo white")

# Creates the title label
title_label = Label(window, text="Kevin and Lawrence's Pizzeria", bg="navajo white", fg="purple4", font="arial 24 bold")
title_label.pack()
# Creates the title photo
photo = PhotoImage(file="roofPizza.gif")
title_image_label = Label(window, image=photo)
title_image_label.pack()

# Creates the name entry label
name_label = Label(window, text="Enter your name:", bg="navajo white", fg="saddle brown", font="arial 12 bold")
name_label.pack()
# Creates the textfield to enter the name
nameEntry = Entry(window, width=20, bg="white")
nameEntry.pack()

# Creates the size option label
size_label = Label(window, text="Select your pizza size:", bg="navajo white", fg="saddle brown", font="arial 12 bold")
size_label.pack()
# Creates a drop-down menu to select the size of the pizza
pizzaSizes = ["Small ($10.99)", "Medium ($12.99)", "Large ($14.99)"]
selectedSize = StringVar(window)
sizeDropDown = OptionMenu(window, selectedSize, *pizzaSizes)
sizeDropDown.pack()

# Creates the crust option label
crust_label = Label(window, text="Enter your crust preference:", bg="navajo white", fg="saddle brown", font="arial 12 bold")
crust_label.pack()
# Creates the crust option radio buttons
selectedCrust = IntVar()
radio1 = Radiobutton(window, text="Hand-Tossed", variable=selectedCrust, value=1)
radio2 = Radiobutton(window, text="Deep-Dish", variable=selectedCrust, value=2)
radio3 = Radiobutton(window, text="Thin-Crust", variable=selectedCrust, value=3)
radio1.pack()
radio2.pack()
radio3.pack()

# Creates the topping selection label
topping_label = Label(window, text="Choose your toppings (additional $1.25 each):", bg="navajo white", fg="saddle brown", font="arial 12 bold")
topping_label.pack()
# Creates the checkbox options to select toppings
pepperoniSelection = IntVar()
checkbox1 = Checkbutton(window, text="Pepperoni", variable=pepperoniSelection)
checkbox1.pack()
sausageSelection = IntVar()
checkbox2 = Checkbutton(window, text="Sausages", variable=sausageSelection)
checkbox2.pack()
mushroomSelection = IntVar()
checkbox3 = Checkbutton(window, text="Mushrooms", variable=mushroomSelection)
checkbox3.pack()
onionSelection = IntVar()
checkbox4 = Checkbutton(window, text="Onions", variable=onionSelection)
checkbox4.pack()

# Creates the topping selection label
place_order_label = Label(window, text="I'M READY!", bg="navajo white", fg="saddle brown", font="arial 12 bold")
place_order_label.pack()
# Creates the button to place the order
place_order = Button(window, text="Place Order", width=15, height=2, command=click)
place_order.pack()

# Creates the text area to generate the receipt
receipt = Text(window, width=22, height=15, wrap=WORD, background="white")
receipt.pack()



window.mainloop()

