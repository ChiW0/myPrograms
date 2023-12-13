import tkinter as tk
from tkinter import *
from tkinter import ttk
import AreaOfCircle

# keep colors in one place
class Color:

    whiteSmoke = "#F7F4F3"
    walnutBrown = "#564D4A"
    cornellRed = "#BA1B1D"


class AppWindow:

    def __init__(self,root):
        self.root = root
        root.title("Circle Area Calculator") # Window title
        root.geometry("210x100") # Default window size
        root.config(bg=Color.whiteSmoke)

        # Question label
        questionLabel = Label(root, text="Enter the radius of a circle:", fg=Color.walnutBrown, bg=Color.whiteSmoke)
        questionLabel.pack()

        # Enter-stuff frame and widgets
        enterFrame = Frame(root, bg=Color.whiteSmoke)
        enterFrame.pack()

        self.enterRadius = Entry(enterFrame, bd=2, bg=Color.whiteSmoke, fg=Color.cornellRed)
        self.enterRadius.pack(side="left", padx=10, pady=10)

        enterButton = Button(enterFrame, text="Enter", bg=Color.walnutBrown, fg=Color.whiteSmoke, command=self.buttonEnter)
        enterButton.pack(side="right", padx=10)

        # Display answer widgets
        answerFrame = Frame(root, bg=Color.whiteSmoke)
        answerFrame.pack()

        self.answerLabel = Label(answerFrame, text="Area = ", fg=Color.cornellRed)
        self.answerLabel.pack(side="bottom", pady=10)
    
    # Passes entered radius to AreaOfCircle.py and changes the result label
    def buttonEnter(self):
        radius = self.enterRadius.get()
        areaResult=AreaOfCircle.calculateCircleArea(radius)
        self.answerLabel.config(text=f"Area = {areaResult}")


# Create main Tkinter window
root = tk.Tk()

# Create an instance of AppWindow class
AppWindow(root)

# Start Tkinter event loop
root.mainloop()