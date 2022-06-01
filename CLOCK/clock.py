import tkinter as tk

root = tk.Tk()
#screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#set the window size
win_width = 500
win_height = 200    

center_x = int(width/2 - win_width/2)
center_y = int(height/2 - win_height/2)

root.geometry(f"{win_width}x{win_height}+{center_x}+{center_y}")
root.title("Digital Clock using Python Tkinter")
root.mainloop()