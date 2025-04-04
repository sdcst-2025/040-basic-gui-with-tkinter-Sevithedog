import tkinter as tk
from tkinter import *
window = tk.Tk()
#window.geometry("200x400")
window.title("T-town Veterinary Clinic Database")
sLabel = tk.Label(window, text = "Search by Name", borderwidth = 3 , relief = "groove")
sEntry = tk.Entry(window)
label1 = tk.Label(window, text = "Client Database")
dog = PhotoImage(window, file="dog.png")
#position
sLabel.grid(row = 1, column = 14)
sEntry.grid(row = 1, column = 16, columnspan= 2)
label1.grid(row = 3, column = 9)
dog.grid(row = 1, column = 2, rowspan = 3, columnspan =2)





window.mainloop()