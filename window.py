import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(width= True, height= True)
        self.root.title("Poke Quiz")

        #Set up style
        s = ttk.Style()
        s.configure('mainFrame.TFrame', background= "#ee1515")

        #Render the frames
        frm = ttk.Frame(self.root, width=800, height=600, padding=10, style= 'mainFrame.TFrame')
        self.root.columnconfigure(index=0, weight=1)
        self.root.rowconfigure(index=1, weight=1)
        frm.grid(sticky='nsew')
        self.root.mainloop()
