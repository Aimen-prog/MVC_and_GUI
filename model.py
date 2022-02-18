#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, nom, prenom, telephone='', adresse='', ville=''):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.adresse = adresse
        self.ville = ville
       # self.id =

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

    def insert_person(self, person):
        if isinstance(person, Person):
            prenom = person.get_prenom()
            nom = person.get_nom()
            self.list_person[f"{prenom} {nom}"] = person

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

    def search_person(self, name):
        names_fetched = []
        for element in self.list_person.keys():
            if name in element:
                names_fetched.append(element)
        print(names_fetched)

    def __str__(self):
        test = ''
        for element in self.list_person:
            test += element
        return test
