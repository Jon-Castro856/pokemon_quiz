import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PokéQuiz")
        self.num= 0

        self.e = Entry(self.root, width= 25, borderwidth= 3)
        self.e.grid(row= 0, column= 0, columnspan= 3, padx= 10, pady= 10)

        bt_1 = Button(self.root, text= '1', padx= 30, pady= 30, command= lambda: self.button_click(1))
        bt_2 = Button(self.root, text= '2', padx= 30, pady= 30, command= lambda: self.button_click(2))
        bt_3 = Button(self.root, text= '3', padx= 30, pady= 30, command= lambda: self.button_click(3))
        bt_4 = Button(self.root, text= '4', padx= 30, pady= 30, command= lambda: self.button_click(4))
        bt_5 = Button(self.root, text= '5', padx= 30, pady= 30, command= lambda: self.button_click(5))
        bt_6 = Button(self.root, text= '6', padx= 30, pady= 30, command= lambda: self.button_click(6))
        bt_7 = Button(self.root, text= '7', padx= 30, pady= 30, command= lambda: self.button_click(7))
        bt_8 = Button(self.root, text= '8', padx= 30, pady= 30, command= lambda: self.button_click(8))
        bt_9 = Button(self.root, text= '9', padx= 30, pady= 30, command= lambda: self.button_click(9))
        bt_0 = Button(self.root, text= '0', padx= 30, pady= 30, command= lambda: self.button_click(0))

        bt_add = Button(self.root, text= '+', padx= 29, pady= 29, command= lambda: self.but_add())
        bt_clear = Button(self.root, text= 'clear', padx= 60, pady= 30, command= lambda: self.but_clear())
        bt_eq = Button(self.root, text= '=', padx= 71, pady= 30, command= lambda: self.but_eq(self.num))

        bt_1.grid(row= 3, column= 0)
        bt_2.grid(row= 3, column= 1)
        bt_3.grid(row= 3, column= 2)
        bt_4.grid(row= 2, column= 0)
        bt_5.grid(row= 2, column= 1)
        bt_6.grid(row= 2, column= 2)
        bt_7.grid(row= 1, column= 0)
        bt_8.grid(row= 1, column= 1)
        bt_9.grid(row= 1, column= 2)
        bt_0.grid(row= 4, column= 0)
        bt_clear.grid(row= 4, column= 1, columnspan= 2)
        bt_add.grid(row= 5, column= 0)
        bt_eq.grid(row= 5, column= 1, columnspan= 2)

        
        self.root.mainloop()

    def button_click(self, n):
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(n))

    def but_clear(self):
        self.e.delete(0, END)

    def but_add(self):
        n1 = self.e.get()
        self.num = int(n1)
        self.e.delete(0, END)

    def but_eq(self, num):
        n2 = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, int(n2) + num)
        

