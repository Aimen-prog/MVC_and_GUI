# coding: utf-8

import os
from tkinter import Button
from tkinter import Entry
from tkinter import filedialog 
from tkinter import Label
from tkinter import Menu
from tkinter import StringVar
from tkinter import Tk
from tkinter import messagebox
"""
Class View of the project


"""

class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.entries = ["Nom", "Prenom", "Telephone", "Adresse", "Ville"]
        self.buttons = ["Chercher", "Inserer", "Effacer"]
        self.modelListFields = []
        self.fileName = None
        self.windows ={}
        self.windows["fenetreResult"] = ...
        self.windows["fenetreErreur"] = ...

    def get_value(self, key):
        return self.widgets_entry[key].get()

    def create_fields(self):
        i, j  = 0, 0

        for idi in self.entries:
            lab = Label(self, text=idi.capitalize())
            self.widgets_labs[idi] = lab
            lab.grid(row=i,column=0)

            var = StringVar()
            entry = Entry(self, text=var)
            self.widgets_entry[idi] = entry
            entry.grid(row=i,column=1)

            i += 1

        for idi in self.buttons:
            buttonW = Button(self, text = idi, command=(lambda button=idi: self.controller.button_press_handle(button)))
            self.widgets_button[idi] = buttonW
            buttonW.grid(row=i+1,column=j)

            j += 1
        
    def display_search(self, person_info) :
        messagebox.showinfo("Results found: ",person_info)
    
    

    
    def main(self):
        print("[View] main")
        self.title("Annuaire")
        self.mainloop()
