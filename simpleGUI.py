import tkinter as tk
from tkinter import *
from tkinter import ttk

# create a root window to display GUI
root = Tk()

# create a frame widget in the root window
frm = ttk.Frame(root, padding=10)

# pack the frame into a grid (columns and rows)
frm.grid()

# creates a label widget that packs in the frame widget, first column and first row
ttk.Label(frm, text="Hello World").grid(column=0, row=0)

# creates a button widget that packs into the frame widget and quits the application when clicked
btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

# event listener. will block any code that comes after it until window is closed. required to run GUI.
root.mainloop()

