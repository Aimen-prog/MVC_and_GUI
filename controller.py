#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Controller class of the program

"""

__author__ = 'Aimen CHERIF'

from view_obj import View
from model import Ensemble
from model import Person

class Controller():
    def __init__(self):
        self.view = View(self)
        self.model = Ensemble()
    
    def start_view(self):
        
        """
        Method interface visibility
        """
        self.view.protocol("WM_DELETE_WINDOW", self.quit_program)
        self.view.create_fields()
        self.view.main()

        
    def search(self):
        
        """
        Method that calls 'search_person' and 'display_search' methods in order to
        display the results for searched persons by their last name.
        if not found, it calls 'search_not_found' and 'empty_field_error' methods of view
        to explain the problem to the user.
        """

        if self.view.get_value("Nom") :
            lname = f"{self.view.get_value('Nom')}"
            
            if self.model.search_person(lname) :
                person_info= self.model.search_person(lname)
                self.view.display_search(person_info)
            else :
                self.view.search_not_found()
                   
        else :
            self.view.empty_field_error()

       
    def delete(self):
        """
        Method that verifies input by calling 'delete_person' method
        if verified (person exists in database annuaire.tsv = deleted from dict),
        it calls 'delete_from_annuaire' method to delete the row(s) from 'annuaire.tsv'
                            (delete by FULL name)
        """
        
        person = Person(self.view.get_value("Nom"),
            self.view.get_value("Prenom"),
            self.view.get_value("Telephone"),
            self.view.get_value("Adresse"),
            self.view.get_value("Ville"))

        if self.model.delete_person(person) : # if deleted from dict then del from db
            self.model.delete_from_annuaire(person)
            self.view.deletion_done() 
        else:
            self.view.deletion_failed() 


    def insert(self):
        """
        Method that verifies input by calling 'insert_person' method
        if verified (person not already present in the database or wrong input), then insert 
        it in the database 'annuaire.tsv'
        """
        person = Person(self.view.get_value("Nom"),
            self.view.get_value("Prenom"),
            self.view.get_value("Telephone"),
            self.view.get_value("Adresse"),
            self.view.get_value("Ville"))

        if self.model.insert_person(person) : # if added to dictionnary then add to db
            self.model.insert_to_annuaire(person)
            self.view.insertion_done() 
        else:
            self.view.insertion_failed()

    def quit_program(self):
        """
        Method that calls "quit_secure" for quit program confirmation 
        """
        self.view.quit_secure()


    def button_press_handle(self, buttonId):
        print("[Controller][button_press_handle] "+ buttonId)
        if buttonId == "Chercher":
            self.search()
        elif buttonId == "Effacer":
            self.delete()
        elif buttonId == "Inserer":
            self.insert()
