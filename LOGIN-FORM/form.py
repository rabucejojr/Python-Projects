from ast import Pass
from cProfile import label
import tkinter as tk
from tkinter import *
from turtle import left

root = Tk()
root.geometry("600x200")
root.grid_columnconfigure((0,1),weight=1)
# labels
username_label = Label(root, text="Username")
password_label = Label(root, text="Password")
#Input fields
username = Text(root, height=1, width=30)
password = Entry(root, show="*", width=30)
#grid
username_label.grid(row=2, column=1)
username.grid(row=2, column=2, sticky=EW)
mainloop()
