import datetime
from tkinter import *
from tkinter.ttk import *
from time import *


###################Function part#############################

def time():
    year = "%Y"
    month = "%B"
    week = "%W"
    hour = "%H:"
    minute = "%M:"
    sec = "%S"
    micro = "%f"

    cltk = datetime.datetime.now().strftime(
        month + " " + year + ", " + "(" + week + ")" + ", " + hour + minute + sec + ":" + micro)
    Label.config(text=cltk)
    Label.after(1000, time)

    print(cltk)


###################gui

root = Tk()
root.title("A clock For Stephanie by Joel Rodriguez")
root.geometry("200x300")
Label = Label(root, font=("ds-digital", 85), background="light blue", foreground="blue")
Label.pack(anchor="center")
time()
root.mainloop()
