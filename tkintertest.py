"""""
# Import Module
from tkinter import *

# create root window
root = Tk()
 
# root window title and dimension
root.title("Wordle Solver")
# Set geometry (widthxheight)
root.geometry('350x200')
 
# all widgets will be here

#Label for Title
title_sentence = Label(root, text = "Wordle Solver")
title_sentence.grid()

#function for button
def clicked():
    new_sentence = input_box.get()
    title_sentence.configure(text = new_sentence)

#button widget with red color text
btn = Button(root, text = "Click this", fg = "red", command = clicked)

#set button grid
btn.grid(column = 0, row = 1)

#add Text Box
input_box = Entry(root, width = 10)
input_box.grid(column = 0, row = 2)

# Execute Tkinter
root.mainloop()
"""

from tkinter import *
from tkinter import ttk

class WordRow:

    def __init__(self, root):

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        self.word = StringVar()
        word_entry = ttk.Entry(mainframe, width=7, textvariable=self.word)
        word_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="word").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        word_entry.focus()
        root.bind("<Return>", self.calculate)
        
    def calculate(self, *args):
        try:
            value = float(self.word.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

root = Tk()
root.title("Wordle Solver")
WordRow(root)
root.mainloop()