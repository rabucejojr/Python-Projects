from tkinter.ttk import *
from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock using Python Tkinter")

def clock():
    tick = strftime("%H:%M:%S")
    clock_label.config(text=tick)
    clock_label.after(1000, clock)
    
#screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#set the window size
win_width = 500
win_height = 200    
#frame size
center_x = int(width/2 - win_width/2)
center_y = int(height/2 - win_height/2)

clock_label = Label(root,font=('sans', 40), fg='black')
clock_label.pack(anchor='center')

root.geometry(f"{win_width}x{win_height}+{center_x}+{center_y}")
clock()
mainloop()