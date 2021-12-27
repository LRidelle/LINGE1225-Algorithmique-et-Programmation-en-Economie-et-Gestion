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
        self.taille = taille
        self.nom = nom

    """
    GETTER
    """
    def getNom(self):
        return self.nom
    
    def getTaille(self):
        return self.taille
    
    """
    SETTER
    """
    def setNom(self, nom):
        self.nom = nom
    
    def setTaille(self, taille):
        if taille>=self.taille:
            self.taille = taille

    #Méthode pour comparer deux objets PauvreChien: A ne pas modifier
    def __eq__(self, autre_chien):
        return self.getNom()==autre_chien.getNom() and self.getTaille()==autre_chien.getTaille()

    def __str__(self):
        return "Nom: {} et Taille: {}".format(self.getNom(),self.getTaille())
        
"""
Classe Maitre

"""
class Maitre:

    #Constructeur
    def __init__(self,nom ,age, chien=None):
        self.nom = nom
        if age<=0:
            age = 0
        self.age = age
        self.chien = chien

    """
    GETTER
    """
    def getNom(self):
        return self.nom
    
    def getAge(self):
        return self.age
    
    def getChien(self):
        return self.chien
    
    """
    SETTER
    """
    def setNom(self, nom):
        self.nom = nom
        
    def setAge(self, age):
        if age>=0:
            self.age = age
    
    def setChien(self, chien):
        self.chien = chien
        
    def aUnChien(self):
        return not self.chien is None

    #Méthode pour comparer deux objets Maitre: A ne pas modifier
    def __eq__(self,autre_maitre):
        return self.getNom()==autre_maitre.getNom() and self.getAge()==autre_maitre.getAge()

    def __str__(self):
        if self.getChien() is None:
            return "Nom: {}  Age: {} ".format(self.getNom(),self.getAge())
        else:
            return "Nom: {}  Age: {}  Chien: {}".format(self.getNom(),self.getAge(), self.getChien().getNom())