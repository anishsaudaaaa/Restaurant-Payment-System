from tkinter import *
import time
import calc_function
import random

root = Tk()
root.geometry("1400x700")
root.title("Restaurant Payment System")

top = Frame(root, width = 1400, height = 50)
top.pack(side=TOP)
frame1 = Frame(root, width = 900, height = 650)
frame1.pack(side=LEFT)
frame2 = Frame(root, width = 400, height = 650)
frame2.pack(side=RIGHT)

app_title = Label(top, font = ('arial', 30, 'bold'), text = "Restaurant Payment System")
app_title.grid(row = 0, column = 0)

localtime = time.asctime(time.localtime(time.time()))
app_time = Label(top, font =('arial', 20), text = localtime)
app_time.grid(row = 1, column = 0)

calc_function.calculator(frame2)

fries = StringVar()
largefries = StringVar()
burger = StringVar()
filet = StringVar()
cheese_burger = StringVar()
drinks = StringVar()
order_no = StringVar()
cost = StringVar()
service_charge = StringVar()
tax = StringVar()
subtotal = StringVar()
total = StringVar()

price_list = {
    "Fries": 100,
    "Large Fries": 150,
    "Burger": 200,
    "Filet": 250,
    "Cheese Burger": 300,
    "Drinks": 50
}

def bill():
    x = str(random.randint(10000, 99999))
    order_no.set(x)

    count_of_fries = int(fries.get())
    count_of_largefries = int(largefries.get())
    count_of_burger = int(burger.get())
    count_of_filet = int(filet.get())
    count_of_cheese_burger = int(cheese_burger.get())
    count_of_drinks = int(drinks.get())

    cost_of_fries = count_of_fries * price_list["Fries"]
    cost_of_largefries = count_of_largefries * price_list["Large Fries"]
    cost_of_burger = count_of_burger * price_list["Burger"]
    cost_of_filet = count_of_filet * price_list["Filet"]
    cost_of_cheese_burger = count_of_cheese_burger * price_list["Cheese Burger"]
    cost_of_drinks = count_of_drinks * price_list["Drinks"]

    cost_of_everything = (cost_of_fries + cost_of_largefries + cost_of_burger +
                    cost_of_filet + cost_of_cheese_burger + cost_of_drinks)
    cost_of_meal = "Rs. %.2f" % cost_of_everything

    PayTax = cost_of_everything * 0.33
    TotalCost = cost_of_everything + PayTax

    ser_charge = TotalCost * 0.125

    service = "Rs. %.2f" % ser_charge
    paid_tax = "Rs. %.2f" % PayTax
    overall_cost = "Rs. %.2f" % TotalCost

    service_charge.set(service)
    cost.set(cost_of_meal)
    tax.set(paid_tax)
    subtotal.set(cost_of_meal)
    total.set(overall_cost)

def exit():
    root.destroy()

def reset():
    fries.set("")
    largefries.set("")
    burger.set("")
    filet.set("")
    cheese_burger.set("")
    drinks.set("")
    order_no.set("")
    cost.set("")
    service_charge.set("")
    tax.set("")
    subtotal.set("")
    total.set("")

def price():
    r = Tk()
    r.geometry("600x220")
    r.title("Price List")

    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "ITEM", fg = 'black', bd = 5)
    lblinfo.grid(row = 0, column = 0)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "_", fg = 'white', bd = 5)
    lblinfo.grid(row = 0, column = 1)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "PRICE", fg = 'white', bd = 5, anchor = W)
    lblinfo.grid(row = 0, column = 2)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Fries", fg = 'steel blue')
    lblinfo.grid(row = 1, column = 0)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Rs." + str(price_list["Fries"]), fg = 'white', bd = 5, anchor = W)
    lblinfo.grid(row = 1, column = 2)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Large Fries", fg = 'steel blue')
    lblinfo.grid(row = 2, column = 0)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Rs." + str(price_list["Large Fries"]), fg = 'white', bd = 5, anchor = W)
    lblinfo.grid(row = 2, column = 2)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Burger", fg = 'steel blue')
    lblinfo.grid(row = 3, column = 0)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Rs." + str(price_list["Burger"]), fg = 'white', bd = 5, anchor = W)
    lblinfo.grid(row = 3, column = 2)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Filet", fg = 'steel blue')
    lblinfo.grid(row = 4, column = 0)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Rs." + str(price_list["Filet"]), fg = 'white', bd = 5, anchor = W)
    lblinfo.grid(row = 4, column = 2)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Cheese Burger", fg = 'steel blue')
    lblinfo.grid(row = 5, column = 0)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Rs." + str(price_list["Cheese Burger"]), fg = 'white', bd = 5, anchor = W)
    lblinfo.grid(row = 5, column = 2)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Drinks", fg = 'steel blue')
    lblinfo.grid(row = 6, column = 0)
    lblinfo = Label(r, font = ('arial', 15, 'bold'), text = "Rs." + str(price_list["Drinks"]), fg = 'white', bd = 5, anchor = W)
    lblinfo.grid(row = 6, column = 2)

    r.mainloop()

lblfries = Label(frame1, font = ('arial', 16, 'bold'), text = "Fries")
lblfries.grid(row = 0, column = 0)

txtfries = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = fries, bd = 6, bg = 'black', justify = 'right')
txtfries.grid(row = 0, column = 1)

lbllargefries = Label(frame1, font = ('arial', 16, 'bold'), text = "Large Fries")
lbllargefries.grid(row = 1, column = 0)

txtlargefries = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = largefries, bd = 6, bg = 'black', justify = 'right')
txtlargefries.grid(row = 1, column = 1)

lblburger = Label(frame1, font = ('arial', 16, 'bold'), text = "Burger")
lblburger.grid(row = 2, column = 0)

txtburger = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = burger, bd = 6, bg = 'black', justify = 'right')
txtburger.grid(row = 2, column = 1)

lblfilet = Label(frame1, font = ('arial', 16, 'bold'), text = "Filet")
lblfilet.grid(row = 3, column = 0)

txtfilet = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = filet, bd = 6, bg = 'black', justify = 'right')
txtfilet.grid(row = 3, column = 1)

lblcheese_burger = Label(frame1, font = ('arial', 16, 'bold'), text = "Cheese Burger")
lblcheese_burger.grid(row = 4, column = 0)

txtcheese_burger = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = cheese_burger, bd = 6, bg = 'black', justify = 'right')
txtcheese_burger.grid(row = 4, column = 1)

lbldrinks = Label(frame1, font = ('arial', 16, 'bold'), text = "Drinks")
lbldrinks.grid(row = 5, column = 0)

txtdrinks = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = drinks, bd = 6, bg = 'black', justify = 'right')
txtdrinks.grid(row = 5, column = 1)


lblorder_no = Label(frame1, font = ('arial', 16, 'bold'), text = "Order No.", fg = 'steel blue')
lblorder_no.grid(row = 0, column = 2)

txtorder_no = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = order_no, bd = 6, bg = 'powder blue', justify = 'right')
txtorder_no.grid(row = 0, column = 3)

lblcost = Label(frame1, font = ('arial', 16, 'bold'), text = "Cost", fg = 'steel blue')
lblcost.grid(row = 1, column = 2)

txtcost = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = cost, bd = 6, bg = 'powder blue', justify = 'right')
txtcost.grid(row = 1, column = 3)

lblservice_charge = Label(frame1, font = ('arial', 16, 'bold'), text = "Service Charge", fg = 'steel blue')
lblservice_charge.grid(row = 2, column = 2)

txtservice_charge = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = service_charge, bd = 6, bg = 'powder blue', justify = 'right')
txtservice_charge.grid(row = 2, column = 3)

lbltax = Label(frame1, font = ('arial', 16, 'bold'), text = "Tax", fg = 'steel blue')
lbltax.grid(row = 3, column = 2)

txttax = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = tax, bd = 6, bg = 'powder blue', justify = 'right')
txttax.grid(row = 3, column = 3)

lblsubtotal = Label(frame1, font = ('arial', 16, 'bold'), text = "Sub Total", fg = 'steel blue')
lblsubtotal.grid(row = 4, column = 2)

txtsubtotal = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = subtotal, bd = 6, bg = 'powder blue', justify = 'right')
txtsubtotal.grid(row = 4, column = 3)

lblTotal = Label(frame1, font = ('arial', 16, 'bold'), text = "Total", fg = 'steel blue')
lblTotal.grid(row = 5, column = 2)

txtTotal = Entry(frame1, font = ('arial', 16, 'bold'), textvariable = total, bd = 6, bg = 'powder blue', justify = 'right')
txtTotal.grid(row = 5, column = 3)

lblTotal = Label(frame1, text = '-', fg = 'white')
lblTotal.grid(row = 6, columnspan = 4)

btnprice = Button(frame1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), width = 10, text = "PRICE",bg = 'powder blue', command = price)
btnprice.grid(row = 7, column = 0)

btntotal = Button(frame1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), width = 10, text = "TOTAL",bg = 'powder blue', command = bill)
btntotal.grid(row = 7, column = 1)

btnreset = Button(frame1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), width = 10, text = "RESET",bg = 'powder blue', command = reset)
btnreset.grid(row = 7, column = 2)

btnexit = Button(frame1, padx = 16, pady = 8, bd = 10, fg = 'black', font = ('arial', 16, 'bold'), width = 10, text = "EXIT",bg = 'powder blue', command = exit)
btnexit.grid(row = 7, column = 3)

root.mainloop()