from tkinter.ttk import *
from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock using Python Tkinter")

clock_label = Label(root, font=('sans', 60), fg='black')

def clock():
    tick = strftime("%H:%M:%S %p")
    clock_label.config(text=tick)
    clock_label.after(1000, clock)
    clock_label.pack(anchor=CENTER)

root.geometry()
clock()
mainloop()
