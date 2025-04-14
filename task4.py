import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("example")
window.geometry("260x150")
#Entities
name = tk.Label(window, text = "Pochacco!")
photo = PhotoImage(file = "dog.png")
dog = tk.Label(window, image = photo)
text = tk.Label(window, text = "A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero",bg = "#87CEEB" )
#positions
dog.place(x = 120, y = 70, anchor=E)
name.place(x = 125, y= 70, anchor = W)
text.place(x = 130, y = 150, anchor = S)
window.mainloop()