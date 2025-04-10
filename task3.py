import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("Example")
#entities
name = tk.Label(window, text = "Pochacco!")
photo = PhotoImage(file = "dog.png")
dog = tk.Label(window, image = photo)
text = tk.Label(window, text = "A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero",bg = "#87CEEB" )
#position
name.grid(row = 3, column = 4)
dog.grid(row = 3, column=3)
text.grid(row = 4, column = 1, columnspan = 5, rowspan = 2)
window.mainloop()