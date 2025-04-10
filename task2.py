import tkinter as tk
from tkinter import *
window = tk.Tk()
#Use sticky to minimize number of columns.
#window.geometry("200x400")
window.title("T-town Veterinary Clinic Database")
yholder = tk.Label(window, text = "       ")
xholder = tk.Label(window, text = "                                                           ")
sLabel = tk.Label(window, text = "Search by Name", borderwidth = 3 , relief = "groove")
sEntry = tk.Entry(window)
label1 = tk.Label(window, text = "Client Database")
dog = PhotoImage(file="dog.png")
doglabel = tk.Label(window, image = dog)
name = tk.Label(window, text = "Name")
nEntry = tk.Entry(window)
type = tk.Label(window, text = "Type")
tEntry = tk.Entry(window)
breed = tk.Label(window, text = "Breed")
bEntry = tk.Entry(window)
owner = tk.Label(window, text = "Owner")
oEntry = tk.Entry(window)
birthday = tk.Label(window, text = "Birthdate")
biEntry = tk.Entry(window)
pbutton = tk.Button(window, text = "<Previous")
save = tk.Button(window, text = "Save Entry")
nbutton = tk.Button(window, text = "Next>")
#position
yholder.grid(row = 1, column = 1, rowspan = 10)
xholder.grid(row = 2, column = 1, columnspan = 18)
sLabel.grid(row = 1, column = 14)
sEntry.grid(row = 1, column = 15, columnspan= 2)
label1.grid(row = 2, column = 12)
doglabel.grid(row = 1, column = 2, rowspan = 3, columnspan =2)
name.grid(row = 5, column = 2, columnspan = 1)
nEntry.grid(row = 6, column = 2, columnspan= 1)
type.grid(row = 5, column = 9, columnspan = 1)
tEntry.grid(row = 6, column = 9, columnspan = 1)
breed.grid(row = 5, column = 12)
bEntry.grid(row = 6, column = 12)
owner.grid(row= 5, column = 14)
oEntry.grid(row = 6, column = 14)
birthday.grid(row = 5, column = 15)
biEntry.grid(row = 6, column = 15)
pbutton.grid(row = 8, column = 1)
save.grid(row = 7, column = 12, rowspan = 1, sticky="s")
nbutton.grid(row = 8, column = 16)
window.mainloop()