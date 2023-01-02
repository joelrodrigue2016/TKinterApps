# importing necessary libraries
from functools import partial
import tkinter as tk

# defining function


def function_name(func):
	print(func)


# creating root window
root = tk.Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
root.geometry("380x400")

# creating button
btn = tk.Button(root, text="Click Me", command=partial(function_name, "Thanks, Geeks for Geeks !!!"))
btn.pack()

# running the main loop
root.mainloop()
