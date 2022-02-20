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
            #lowercasing them to help control duplicates afterwards

    def insert_to_annuaire(self,person):
        """
        Method that allows to update the 'annuaire.tsv' database 
        
        """

        with open('annuaire.tsv', 'a') as annuaire:
            writer = csv.writer(annuaire, delimiter='\t')
            writer.writerow([person.nom, person.prenom, person.telephone, 
                                  person.adresse, person.ville])
            
            
    def delete_from_annuaire(self,person):
        """
        Method that allows to update the 'annuaire.tsv' database after deletion
        using a only person last name recuperated from the interface
        Note: new file "annuaire_after_deletion.tsv" is created and like for searching
        method if many persons with same last name it deletes them all ;).
 
        """

        filePath = "annuaire.tsv"
        with open(filePath)	as f:
            reader = csv.DictReader(f, delimiter='\t')
            
            filePath = "annuaire_after_deletion.tsv"
            with open(filePath,'w',newline='') as f:
                fieldnames = ["Nom", "Prenom", "Telephone", "Adresse", "Ville"]
                writer = csv.DictWriter(f,fieldnames=fieldnames, delimiter='\t')
                deletion = person.nom.lower()
                
                for row in reader:
                    if deletion != row['Nom'].lower():
                        writer.writerow(row) ; # write all non-matching rows
                    else:
                        print("Deleted") # nothing to write


    def insert_person(self, person):
        
        """
        First, this method allows the dict to be updated from the annuaire database.
        Then, it adds a Person object's full name to the dict. 
        It's not allowing duplicated full names because of key unicity property.
        
        It returns TRUE when new person is added (dict length changed)
        FALSE when wrong data input/isn't Person instance or duplicated names(unchanged length)

        """
        self.update_person_dict()
        init_dict_len= len(self.list_person) #initial length of dict
        
        if len(person.nom.replace(" ", "")) == 0 and len(person.prenom.replace(" ", "")) == 0 or (person.nom.isalnum() or person.prenom.isalnum()):
            return False #bad full name input
        else :
            if isinstance(person, Person) :
                prenom = person.get_prenom().lower()
                nom = person.get_nom().lower()
                self.list_person[f"{prenom} {nom}"] = person #dict updated but by stacking!
                
                curr_dict_len= len(self.list_person) #current length of dict      
                if curr_dict_len != init_dict_len :
                    return True #to be added (not duplicated) 
                else:
                    return False #not to be added to the database (duplicated)
            else :
                return False #not an instance of person
        

    def delete_person(self, person):
        """
        Method that deletes a person from dictionnary prevously updated from database.
        Returns True if deleted. False if not.
        """
        self.update_person_dict()
        init_dict_len= len(self.list_person) #initial length of dict
        
        if isinstance(person, Person):
            prenom = person.get_prenom()
            nom = person.get_nom()
            values_to_del = []

            for element in self.list_person.keys():
                if prenom in element or nom in element:
                    values_to_del.append(element)

            for to_del in values_to_del:
                del self.list_person[to_del]
                curr_dict_len= len(self.list_person) #initial length of dict
                if init_dict_len!=curr_dict_len: #dict length changed
                    return True #to be deleted from db
                else:
                    return False #not to be deleted
        else :
            return False #not an instance of person


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










