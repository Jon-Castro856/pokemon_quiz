import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        #initialize window
        self.root = tk.Tk()
        self.root.title("PokéQuiz")
        self.root.geometry('800x600')
        
        self.init_start()
        self.frame.pack()
        self.root.mainloop()

    def init_start(self):
        #initialize grid for placement
        self.frame = ttk.Frame(self.root, height= 600, width= 800)
        self.frame.rowconfigure(0, weight= 1)
        self.frame.columnconfigure(0, weight= 1)

        #create widgets to place on grid
        greetings = ttk.Label(self.frame, text= "Welcome to the Pokémon Quiz!", font=('Arial', 36))
        start = ttk.Button(self.frame, text="Start Quiz")
        quit = ttk.Button(self.frame, text= "Quit", command= self.root.destroy)
        greetings.grid(row= 0, column= 0)
        start.grid(row= 1, column= 0, pady= 50, rowspan= 1)
        quit.grid(row= 2, column= 0, pady= 50)