#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

from DataCollectionForm import schoolentry


class PersonalDataForm:
    def __init__(self, master=None):
        # build ui
        personalform = tk.Tk() if master is None else tk.Toplevel(master)
        personalform.configure(
            cursor="arrow",
            height=200,
            highlightbackground="#00ff40",
            highlightcolor="#d22dc1",
            width=200)
        personalform.geometry("384x288")
        personalform.resizable(False, False)

        # name
        self.namelabl = tk.Label(personalform)
        self.namelabl.configure(text='Name')
        self.namelabl.pack(side="top")
        self.nameentry = tk.Entry(personalform)
        self.nameentry.configure(font="TkDefaultFont")
        self.nameentry.pack(side="top")

        # lastname
        self.lastnamelbl = tk.Label(personalform)
        self.lastnamelbl.configure(text='Lastname')
        self.lastnamelbl.pack(side="top")
        self.lastnameentry = tk.Entry(personalform)
        self.lastnameentry.pack(side="top")
        # nationality
        self.nationalitylbl = tk.Label(personalform)
        self.nationalitylbl.configure(text='Nationality')
        self.nationalitylbl.pack(side="top")
        self.nationalityentry = tk.Entry(personalform)
        self.nationalityentry.pack(side="top")
        # Age
        self.agelab = tk.Label(personalform)
        self.agelab.configure(text='Age')
        self.agelab.pack(side="top")
        self.ageentry = tk.Entry(personalform)
        self.ageentry.pack(side="top")
        # Address
        self.addresslab = tk.Label(personalform)
        self.addresslab.configure(text='Address')
        self.addresslab.pack(side="top")
        self.addressebtry = tk.Entry(personalform)
        self.addressebtry.pack(side="top")
        # School
        self.schoollab = tk.Label(personalform)
        self.schoollab.configure(text='School')
        self.schoollab.pack(side="top")
        self.schoolentry = tk.Entry(personalform)
        self.schoolentry.pack(side="top")
        # Ok Button
        self.submitbtn = tk.Button(personalform)
        self.submitbtn.configure(text='Submit')
        self.submitbtn.pack(fill="both", side="top")
        self.submitbtn = ttk.Button(personalform,text="ok", command=self.submitFunction)

        # Clear Button
        self.clearbtn = tk.Button(personalform)
        self.clearbtn.configure(text='CLEAR')
        self.clearbtn.pack(fill="both", side="top")
        self.clearbtn.configure(text='CLEAR')

        self.clearbtn.pack()

        # Main widget
        self.mainwindow = personalform

    def clearFunction(self):
        print('Clear button is clicked.')

    def submitFunction(self):
        print(schoolentry.get())

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = PersonalDataForm()
    app.run()
