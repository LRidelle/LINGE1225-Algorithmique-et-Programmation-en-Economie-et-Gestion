#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:44:40 2021

@author: louisridelle

TP06 - EXERCICE 2
"""
"""
Classe Voiture

"""
class Voiture:

    def __init__(self, vitesse=0):
        self.vitesse = 0
    
    def incre(self, vitesse=1):
        if self.vitesse + vitesse<=5 and vitesse>=0:
            self.vitesse += vitesse
    
    def decre(self, vitesse=1):
        if self.vitesse - vitesse>=-1 and vitesse>=0:
            self.vitesse -= vitesse
            
    def vitesse_actuelle(self):
        return self.vitesse
    
    #A ne pas modifier
    def __str__(self):
        return 'Vitesse actuelle: {}'.format(self.vitesse_actuelle())