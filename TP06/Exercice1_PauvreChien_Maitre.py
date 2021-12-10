#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 18:56:34 2021

@author: louisridelle

TP06 - EXERCICE 1
"""
"""
Classe PauvreChien

"""

class PauvreChien:

    # Constructeur
    def __init__(self,  taille, nom=""):
        if taille<=0:
            taille = 0
        self.__taille = taille
        self.__nom = nom

    #Méthode pour comparer deux objets PauvreChien: A ne pas modifier
    def __eq__(self,autre_chien):
        return self.getNom()==autre_chien.getNom() and self.getTaille()==autre_chien.getTaille()

    def __str__(self):
        return "Nom: {} et Taille: {}".format(self.getNom(),self.getTaille())

    """
    GETTER
    """
    def getNom(self):
        return self.__nom
    
    def getTaille(self):
        return self.__taille
    
    """
    SETTER
    """
    def setNom(self, nom):
        self.__nom = nom
    
    def setTaille(self, taille):
        if taille>=self.__taille:
            self.__taille = taille
        
"""
Classe Maitre

"""
class Maitre:

    #Constructeur
    def __init__(self,nom ,age, chien=None):
        self.__nom = nom
        if age<=0:
            age = 0
        self.__age = age
        self.__chien = chien

    #Méthode pour comparer deux objets Maitre: A ne pas modifier
    def __eq__(self,autre_maitre):
        return self.getNom()==autre_maitre.getNom() and self.getAge()==autre_maitre.getAge()

    def __str__(self):
        if self.getChien() is None:
            return "Nom: {}  Age: {} ".format(self.getNom(),self.getAge())
        else:
            return "Nom: {}  Age: {}  Chien: {}".format(self.getNom(),self.getAge(), self.getChien().getNom())
    
    """
    GETTER
    """
    def getNom(self):
        return self.__nom
    
    def getAge(self):
        return self.__age
    
    def getChien(self):
        return self.__chien
    
    """
    SETTER
    """
    def setNom(self, nom):
        self.__nom = nom
        
    def setAge(self, age):
        if age>=0:
            self.__age = age
    
    def setChien(self, chien):
        self.__chien = chien
        
    def aUnChien(self):
        return not self.__chien is None