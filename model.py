#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

class Person:
    def __init__(self, nom, prenom, telephone='', adresse='', ville=''):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.adresse = adresse
        self.ville = ville

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_telephone(self):
        return self.telephone

    def get_adresse(self):
        return self.adresse

    def get_ville(self):
        return self.ville

    def __str__(self):
        return self.get_nom()+self.get_prenom()+self.get_telephone()+self.get_adresse()+self.get_ville()


class Ensemble:
    def __init__(self):
        self.list_person = {}
        
    def update_person_dict(self):
        """
        Method that updates the dictionnary of the class from 'annuaire.tsv' database
        
        """

        with open('annuaire.tsv', 'r') as annuaire:
            reader = csv.DictReader(annuaire, delimiter='\t')
            for row in reader:
                self.list_person['%s %s'% (
                            row['Prenom'].lower(),
                            row['Nom'].lower())]= Person 
            #lowercasing them to help control duplicates below

    def insert_person(self, person):
        
        """
        Method that allows class dictionnary to be updated from the database
        then adds a Person object to the dictionnary if it is an instance of Person and
        that it's unique (not allowing duplicated names and last names)
        
        Note: class dictionnary is used as a transitory structure between db "annuaire.tsv"
        and insertion process
        """
        self.update_person_dict()
        if isinstance(person, Person) and f"{person.prenom} {person.nom}".lower() not in self.list_person:
            prenom = person.get_prenom()
            nom = person.get_nom()
            self.list_person[f"{prenom} {nom}"] = person
            return True
        else :
            return False

    def delete_person(self, person):
        if isinstance(person, Person):
            prenom = person.get_prenom()
            nom = person.get_nom()
           # del self.list_person[]
            values_to_del = []
            for element in self.list_person.keys():
                if prenom in element or nom in element:
                    values_to_del.append(element)
            for to_del in values_to_del:
                del self.list_person[to_del]
                print('Deleted: '+to_del)
                             


    def search_person(self, lname, person_fetched = ''):
        
        """
        Method that searches a person in a database (annuaire) by its last name 
        and returns its corresponding informations.
        If many persons with same last name, it returns all of these persons. ;) 
        """
        
        with open('annuaire.tsv', 'r') as annuaire:
            reader = csv.DictReader(annuaire, delimiter='\t')
            for row in reader:
                if lname.lower() == row['Nom'].lower():
                    person_fetched += '\nPrenom : %s\nNom: %s\nTelephone: %s\nAdresse: %s\nVille: %s\n'% (
                            row['Prenom'],
                            row['Nom'],
                            row['Telephone'],
                            row['Adresse'],
                            row['Ville'])
                    
        return person_fetched   
        



    def __str__(self):
        test = ''
        for element in self.list_person:
            test += element
        return test










