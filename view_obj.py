#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
View class of the program

"""
__author__ = 'Aimen CHERIF'

from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk
from tkinter import messagebox


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.entries = ["Nom", "Prenom", "Telephone", "Adresse", "Ville"]
        self.buttons = ["Chercher", "Inserer", "Effacer"]


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
            button_w = Button(self, text = idi, command=(lambda button=idi: self.controller.button_press_handle(button)))
            self.widgets_button[idi] = button_w
            button_w.grid(row=i+1,column=j)

            j += 1

    def display_search(self, person_info) :

        """Method displaying message box showing searched person(s) informations"""

        messagebox.showinfo("Results found:", person_info)

    def empty_field_error(self) :

        """Method displaying an error message: empty last name field."""

        messagebox.showerror('Error', 'Last name field must be filled!')

    def search_not_found(self) :

        """Method displaying a warning message: empty last name field."""

        messagebox.showwarning('Warning', 'No results found, nothing matches!')

    def insertion_done(self) :

        """Method displaying a successful insertion message"""

        messagebox.showinfo('Insertion status', 'Insertion successfully done!')

    def insertion_failed(self) :

        """Method displaying an error message: person (full name) already in the database
        or empty input"""

        messagebox.showerror('Insertion status', 'Insertion FAILED!\nPossible reasons:\n-Person exists already\n-Empty full name fields')

    def deletion_done(self) :

        """Method displaying a successful deletion message"""
        messagebox.showinfo('Deletion status', 'Deletion successfully done!')

    def deletion_failed(self) :

        """Method displaying an error message: person (Full name= last+st names) not
        in the database "annuaire.tsv" or empty input"""

        messagebox.showerror('Deletion status', 'Deletion FAILED!\nPossible reasons:\n-Person unavailable in database\n-Empty full name fields')

    def clearup(self):
        """
        Method that clears entries after button clicks
        """
        for idi in self.widgets_entry:
            self.widgets_entry[idi].delete(0, "end")


    def quit_secure(self):
        response = messagebox.askokcancel("Quit", "Are you sur you want to quit?")
        if response:
            self.destroy()

    def main(self):
        print("[View] main")
        self.title("Annuaire")
        self.mainloop()
