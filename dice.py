from random import randint, random
from tkinter import *   
from tkinter import ttk
from turtle import width, window_width 


def diceRoll(*args):
    try:
        roll.set(randint(1,6))
    except ValueError:
        pass


root = Tk()
root.title("Dice")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("200x100")

ttk.Label(mainframe, text="Roll the Dice!").grid(column=1, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Dice Roll", command=diceRoll).grid(column=1, row=2, sticky=W)

roll = StringVar()
ttk.Label(mainframe, textvariable=roll).grid(column=1, row=3, sticky=(W, E))


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    

root.bind("<Return>", diceRoll)

root.mainloop()


