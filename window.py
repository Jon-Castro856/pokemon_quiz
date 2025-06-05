import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        #initialize window
        self.root = tk.Tk()
        self.root.title("PokéQuiz")
        #self.root.geometry('800x600')
        
        self.init_start()
        self.startframe.pack()
        self.root.mainloop()

    def init_start(self):
        #initialize grid for placement
        self.startframe = ttk.Frame(self.root)
        self.startframe.rowconfigure(0, weight= 1)
        self.startframe.rowconfigure(1, weight= 1)
        self.startframe.rowconfigure(2, weight= 1)
        self.startframe.columnconfigure(0, weight= 1)

        #create widgets to place on grid
        greetings = ttk.Label(self.startframe, text= "Welcome to the Pokémon Quiz!", font=('Arial', 36))
        start = ttk.Button(self.startframe, text="Start Quiz", command= lambda: self.start_quiz())
        quit = ttk.Button(self.startframe, text= "Quit", command= self.root.destroy)
        greetings.grid(row= 0, column= 0)
        start.grid(row= 1, column= 0, pady= 50)
        quit.grid(row= 2, column= 0, pady= 50)

    def start_quiz(self):
        self.startframe.destroy()
        self.quiz_frame = ttk.Frame(self.root)
        self.init_quiz_frame()

    def init_quiz_frame(self):
        self.quiz_frame.rowconfigure(0, weight= 1)
        self.quiz_frame.rowconfigure(1, weight= 1)
        self.quiz_frame.rowconfigure(2, weight= 1)
        self.quiz_frame.rowconfigure(3, weight= 1)
        self.quiz_frame.rowconfigure(4, weight= 1)
        self.quiz_frame.columnconfigure(0, weight= 1)
        self.quiz_frame.columnconfigure(1, weight= 1)
        self.quiz_frame.columnconfigure(2, weight= 1)
        self.quiz_frame.pack()
        
        picture = ttk.Label(self.quiz_frame, width= 96, text= "Image goes here")
        picture.grid(row= 0, column= 0)