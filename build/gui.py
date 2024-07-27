#This File was created by Joel Rodriguez and designed in Figma

import sqlite3
from pathlib import Path
#from Personalfigma import *
# from tkinter import * 
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Joel\Documents\Python\tkinter\TKinter_Figma\Tutorial\build\assets\frame0")
conn=sqlite3.connect("personalfigma.db")
cur = conn.cursor()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x400")
window.configure(bg = "#FFFFFF")

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")


def insert_data(name, lastname, age, nationality, occupation):
    data_insert_query = data_insert_query = '''INSERT INTO personal(name, lastname, nationality, age, occupation) VALUES(?, ?, ?, ?, ?)'''
    data_insert_tuple = (name, lastname, nationality, age, occupation)
    cur.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    print("Data inserted")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    300.0,
    0.0,
    600.0,
    400.0,
    fill="#1E6837",
    outline="")

canvas.create_text(
    336.0,
    37.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("Calistoga Regular", 12 * -1)
)
##################################################################################################
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    443.5,
    70.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=336.0,
    y=61.0,
    width=215.0,
    height=17.0
)
entry_1.bind("<Tab>", focus_next_widget)
canvas.create_text(
    336.0,
    92.0,
    anchor="nw",
    text="Last name",
    fill="#FFFFFF",
    font=("Calistoga Regular", 12 * -1)
)

canvas.create_text(
    336.0,
    147.0,
    anchor="nw",
    text="Age",
    fill="#FFFFFF",
    font=("Calistoga Regular", 12 * -1)
)
##################################################################################################
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    443.5,
    180.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=336.0,
    y=171.0,
    width=215.0,
    height=17.0
)
entry_2.bind("<Tab>", focus_next_widget)
canvas.create_text(
    336.0,
    199.0,
    anchor="nw",
    text="Nationality",
    fill="#FFFFFF",
    font=("Calistoga Regular", 12 * -1)
)
##################################################################################################
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    443.5,
    232.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=336.0,
    y=223.0,
    width=215.0,
    height=17.0
)
canvas.create_text(
    336.0,
    254.0,
    anchor="nw",
    text="Occupation",
    fill="#FFFFFF",
    font=("Calistoga Regular", 12 * -1)
)
entry_3.bind("<Tab>", focus_next_widget)
##################################################################################################
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    443.5,
    287.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=336.0,
    y=278.0,
    width=215.0,
    height=17.0
)
entry_4.bind("<Tab>", focus_next_widget)
##################################################################################################
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    443.5,
    125.5,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=336.0,
    y=116.0,
    width=215.0,
    height=17.0
)
entry_5.bind("<Tab>", focus_next_widget)


##################################################################################################
##################################################################################################







button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insert_data(
        entry_1.get("1.0", "end-1c"),
        entry_5.get("1.0", "end-1c"),
        entry_2.get("1.0", "end-1c"),
        entry_3.get("1.0", "end-1c"),        
        entry_4.get("1.0", "end-1c"), ),
    relief="flat"
)
button_1.place(
    x=368.0,
    y=322.0,
    width=164.0,
    height=43.0
)

button_image_hover_1 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(
        image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
        image=button_image_1
    )

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    150.0,
    200.0,
    image=image_image_1
)


window.resizable(False, False)
window.mainloop()
