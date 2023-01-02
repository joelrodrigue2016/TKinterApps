from tkinter import *
import tkinter as tk
from tkinter import ttk
from sqlite3 import connect
##C:\Users\Joel\anaconda3\envs\rstudio\Scripts
#from DataCollectionFormSQL import *

"""Functions"""


def clearFunction():
    nameentry.delete(0, END)
    lastnameentry.delete(0, END)
    nationalityentry.delete(0, END)
    ageentry.delete(0, END)
    addressebtry.delete(0, END)
    schoolentry.delete(0, END)


"""Form"""
base = Tk()
base.geometry('500x400')
base.title("Registration Form")
base.resizable(False, False)
# labl_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
# labl_0.place(x=90, y=53)


# name
namelabl = tk.Label(base)
namelabl.configure(text='Name')
namelabl.pack(side="top")
nameentry = tk.Entry(base)
nameentry.configure(font="TkDefaultFont")
nameentry.pack(side="top")

# lastname
lastnamelbl = tk.Label(base)
lastnamelbl.configure(text='Lastname')
lastnamelbl.pack(side="top")
lastnameentry = tk.Entry(base)
lastnameentry.pack(side="top")
# nationality
nationalitylbl = tk.Label(base)
nationalitylbl.configure(text='Nationality')
nationalitylbl.pack(side="top")
nationalityentry = tk.Entry(base)
nationalityentry.pack(side="top")
# Age
agelab = tk.Label(base)
agelab.configure(text='Age')
agelab.pack(side="top")
ageentry = tk.Entry(base)
ageentry.pack(side="top")
# Address
addresslab = tk.Label(base)
addresslab.configure(text='Address')
addresslab.pack(side="top")
addressebtry = tk.Entry(base)
addressebtry.pack(side="top")
# School
schoollab = tk.Label(base)
schoollab.configure(text='School')
schoollab.pack(side="top")
schoolentry = tk.Entry(base)
schoolentry.pack(side="top")


def submitFunction():
    try:

        conn = connect('personal.db')
        cur = conn.cursor()
        ################################################
        name = nameentry.get()
        lastname = lastnameentry.get()
        nationality = nationalityentry.get()
        age = ageentry.get()
        address = addressebtry.get()
        school = schoolentry.get()
        #################################################
        # Insert Data
        data_insert_query = '''INSERT INTO personal (name, lastname, nationality,  age, address,school) VALUES  (?, ?, ?, ?, ?, ?)'''
        data_insert_tuple = (name, lastname, nationality, age, address, school)

        cur.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()
        print("Data entered successfully!!!!")
        conn.close()
    except Exception as e:
        print(e)


# Main widget
mainwindow = base

Button(base, text='Submit', width=30, bg='brown', fg='white', command=submitFunction).place(x=150, y=280)
Button(base, text='Clear', width=30, bg='brown', fg='white', command=clearFunction).place(x=150, y=310)
# it will be used for displaying the registration form onto the window
base.mainloop()
print("ok")


def main():
    submitFunction()



if __name__ == "__main__":
    main()
