from tkinter import *
from tkinter import ttk
from Roll import *


class Window:
    def __init__(self):
        self.root = Tk()
        self.roll = Roll();
        self.roll_result = StringVar()
        self.root.title("Dice")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # type: ignore
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("200x100")
        ttk.Label(self.mainframe, text="Roll the Dice!").grid(column=1, row=1, sticky=(W, E)) # type: ignore
        ttk.Button(self.mainframe, text="Dice Roll", command=self.diceRoll).grid(column=1, row=2, sticky=W)
    
    def diceRoll(self):
        roll_value = self.roll.roll_dice()
        self.roll_result.set(str(roll_value))
        
        ttk.Label(self.mainframe, textvariable=self.roll_result).grid(column=1, row=3, sticky=(W, E)) # type: ignore

if __name__ == "__main__":      
    window = Window()
    window.root.mainloop()