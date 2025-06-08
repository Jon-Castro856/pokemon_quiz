import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        #initialize window
        self.root = tk.Tk()
        self.root.title("PokéQuiz")
        self.root.geometry(self.center_window(800, 600))

        #initialize variables
        self.answer1 = None
        self.answer2 = None
        self.answer3 = None
        self.answer4 = None
        self.correct = None
        self.total = 0
        self.curr = 1
        
        self.init_start()
        self.startframe.pack()
        self.root.mainloop()
    
    def center_window(self, width, height): #makes sure window spawns at the same spot
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        x = int(((self.screen_width/2) - (width)))
        y = int(((self.screen_height/2) - (height)))
        return f"{width}x{height}+{x}+{y}"

    def init_start(self): #create start screen and place its content on screen
        self.startframe = ttk.Frame(self.root)
        self.startframe.rowconfigure(0, weight= 1)
        self.startframe.rowconfigure(1, weight= 1)
        self.startframe.rowconfigure(2, weight= 1)
        self.startframe.rowconfigure(3, weight= 1)
        self.startframe.columnconfigure(0, weight= 1)

        #create widgets to place on grid
        greetings = ttk.Label(self.startframe, text= "Welcome to the Pokémon Quiz!", font=('Arial', 36))
        start = ttk.Button(self.startframe, text="Start Quiz", command= lambda: self.start_quiz())
        quit = ttk.Button(self.startframe, text= "Quit", command= self.root.destroy)
        description = ttk.Label(self.startframe, text= "In this 5 question quiz, you'll have to pick which attribute doesn't match up with the displayed pokemon!")
        greetings.grid(row= 0, column= 0)
        start.grid(row= 1, column= 0, pady= 50)
        quit.grid(row= 3, column= 0, pady= 50)
        description.grid(row= 2, column= 0)

    def start_quiz(self):
        self.startframe.destroy()
        self.init_quiz_frame()

    def init_quiz_frame(self): #create quiz frame and place its content onto the screen
        self.quiz_frame = ttk.Frame(self.root)
        self.quiz_frame.rowconfigure(0, weight= 1)
        self.quiz_frame.rowconfigure(1, weight= 1)
        self.quiz_frame.rowconfigure(2, weight= 1)
        self.quiz_frame.rowconfigure(3, weight= 1)
        self.quiz_frame.rowconfigure(4, weight= 1)
        self.quiz_frame.columnconfigure(0, weight= 1)
        self.quiz_frame.columnconfigure(1, weight= 1)
        self.quiz_frame.columnconfigure(2, weight= 1)
        self.quiz_frame.columnconfigure(3, weight= 1)
        self.quiz_frame.pack()
        
        #initialize quiz content
        picture = ttk.Label(self.quiz_frame, width= 48, text= "Image goes here")
        question = ttk.Label(self.quiz_frame, padding= 10, text= "Which of these is incorrect?")
        curr_question = ttk.Label(self.quiz_frame, text= f"Question #{self.curr}")
        answer_count = ttk.Label(self.quiz_frame, text= f"Correct answers: {self.total}")
        
        select1 = ttk.Button(self.quiz_frame, text= "aaa", command= lambda: self.check_answer(self.answer1))
        select2 = ttk.Button(self.quiz_frame, text= "bbb", command= lambda: self.check_answer(self.answer2))
        select3= ttk.Button(self.quiz_frame, text= "ccc", command= lambda: self.check_answer(self.answer3))
        select4 = ttk.Button(self.quiz_frame, text= "ddd", command= lambda: self.check_answer(self.answer4))

        #place content onto screen
        picture.grid(row= 0, column= 0)
        question.grid(row= 1, column= 0)
        curr_question.grid(row= 0, column= 2)
        answer_count.grid(row= 1, column= 2)
        select1.grid(row= 2, column= 0, pady= 10)
        select2.grid(row= 2, column= 1)
        select3.grid(row= 3, column= 0, pady= 10)
        select4.grid(row= 3, column= 1)

    def check_answer(self, answer): #check if the answer is correct, and update the relevant variables
        if answer == self.correct:
            self.total += 1
            self.curr += 1
            self.quiz_frame.destroy()
            self.init_correct()
        else:
            self.curr += 1
            self.quiz_frame.destroy()
            self.init_incorrect()
                
    def init_correct(self):
        correct = ttk.Label(self.root, text= "Correct!", font=('Arial', 36))
        correct.pack(anchor= "center")
        correct.after(2000, self.next, correct)

    def init_incorrect(self):
        incorrect = ttk.Label(self.root, text= "Incorrect!", font=('Arial', 36))
        incorrect.pack(anchor= "center")
        incorrect.after(2000, self.next, incorrect)

    def next(self, label): #remove label and return to quiz, or end the quiz after the 5th question
        label.destroy()
        if self.curr > 5:
            self.init_end_screen()
        else:
            self.init_quiz_frame()

    def init_end_screen(self): #show them how many questions they got right, and offer to replay quiz
        end = ttk.Frame(self.root)
        finish = ttk.Label(end, text= f"You got {self.total} questions right!", font=('Arial', 36))
        replay = ttk.Button(end, text= "Play Again?", command= lambda: self.replay(end))
        end.pack()
        finish.grid(row= 0, column= 0)
        replay.grid(row= 1,  column= 0, pady= 10)

    def replay(self, frame): #reset score, return to start
        frame.destroy()
        self.curr = 1
        self.total = 0
        self.init_quiz_frame()
