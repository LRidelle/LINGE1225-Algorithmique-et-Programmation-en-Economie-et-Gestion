#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:45:53 2021

@author: louisridelle

TP06 - EXERCICE 4
"""
"""
Classe Personne

"""
class Personne:

    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    #A ne pas modifier
    def __eq__(self,autre_personne):
        if autre_personne is None:
            return None
        return self.getPrenom()==autre_personne.getPrenom() and self.getAge()==autre_personne.getAge()

    def vieillir(self):
        self.__age += 1
    
    """
    GETTER
    """
    def getPrenom(self):
        return self.__nom
    
    def getAge(self):
        return self.__age

    #A ne pas modifier
    def __str__(self):
        return "Prenom: {} et Âge: {}".format(self.getPrenom(),self.getAge())

"""
Classe Homme

"""
class Homme(Personne):

    def __init__(self, nom, age, epouse=None):
        super().__init__(nom, age)
        self.__epouse = epouse

    #A ne pas modifier
    def __eq__(self,autre_homme):
        return super().__eq__(autre_homme) and self.getEpouse() ==autre_homme.getEpouse()

    def celibat(self):
        return self.__epouse is None
        
    def getEpouse(self):
        if self.celibat():
            return None
        return self.__epouse
        
    def setEpouse(self, f):
        self.__epouse = f
        
    def marier(self,f):
        if self.celibat() and f.celibat() and self.getAge()>=18 and f.getAge()>=18:
            self.__epouse = f
            f.setEpoux(self)

    # A ne pas modifier
    def __str__(self):
        if self.getEpouse() is None:
            return super().__str__()
        else:
            return super().__str__() +" Epouse: {}".format(self.getEpouse().getPrenom())

"""
Classe Femme

"""
class Femme(Personne):

    def __init__(self, nom, age, epoux=None):
        super().__init__(nom, age)
        self.__epoux = epoux

    #A ne pas modifier
    def __eq__(self,autre_femme):
        return super().__eq__(autre_femme) and self.getEpoux() ==autre_femme.getEpoux()

    def celibat(self):
        return self.__epoux is None
        
    def getEpoux(self):
        if self.celibat():
            return None
        return self.__epoux
        
    def setEpoux(self, h):
        self.__epoux = h
        
    def marier(self,h):
        if self.celibat() and h.celibat() and self.getAge()>=18 and h.getAge()>=18:
            self.__epoux = h
            h.setEpouse(self)

    # A ne pas modifier
    def __str__(self):
        if self.getEpoux() is None:
            return super().__str__()
        else:
            return super().__str__() +" Epouse: {}".format(self.getEpoux().getPrenom())
        
h = Homme("Victor", 23, None)
f = Femme("Emma", 24, None)
f.marier(h)
print(h.celibat())
print(f.celibat())
print(f.getAge()>=18)
print(f)
print(h)
