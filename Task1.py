import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("tk")
button1 = tk.Button(window, bg = "#FF0000")
button2 = tk.Button(window, bg = "#FFFF00")
button3 = tk.Button(window, bg = "#008000")
box1 = tk.Entry(window)
box2 = tk.Label(window, text = "x")
box3 = tk.Entry(window)
box4 = tk.Label(window, text = "=" ,borderwidth= 2, relief = "groove")
box5 = tk.Entry(window)
spacer = tk.Label(window, text ="")
button1.grid(row = 1, column = 1)
button2.grid(row = 1, column =2)
button3.grid(row = 1, column = 3)
box1.grid(row = 2 , column=2, columnspan= 2 )
box2.grid(row = 2, column = 6)
box3.grid(row = 2, column = 8, columnspan=2 )
box4.grid(row = 2, column = 11 )
box5.grid(row = 2, column=13, columnspan=4)
spacer.grid(row = 3, column = 1, columnspan=12)



window.mainloop()