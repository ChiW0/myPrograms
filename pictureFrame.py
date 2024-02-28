import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Picture Frame")

pictureFrame = Frame(root, bg="#3f1010")
pictureFrame.pack(side="top")

def pictureSelect():
    print("This photo hasn't been purchased yet.")

image = PhotoImage(file="downwardgaze.gif")
img_resize = image.subsample(2,2)
photoBtn = Button(pictureFrame, image=img_resize, command=pictureSelect, bg="white", relief=SUNKEN)
photoBtn.pack(padx=20, pady=20)

wall = Frame(root, bg="#adbce6")
wall.pack(fill="both", expand=True)

pictureTitle = Label(wall, bd=2, bg="#aaaaaa", text="downwardgaze \n Uknown")
pictureTitle.pack(side="top", pady=10)

root.mainloop()