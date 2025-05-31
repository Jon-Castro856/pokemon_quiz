import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        bg = Image.open('images/bg.png')

        bg = ImageTk.PhotoImage(bg)
        bg_label = tk.Label(self.root, image= bg)
        bg_label.place(x= 0, y= 0, relwidth= 1, relheight= 1)
        bg_label.image = bg
        start_bt = ttk.Button(self.root, text= 'Start')
        quit_bt = ttk.Button(self.root, text= 'Quit', command= self.root.destroy)

        start_bt.place(x= 355, y= 200)
        quit_bt.place(x= 355, y= 400)
        self.root.mainloop()
