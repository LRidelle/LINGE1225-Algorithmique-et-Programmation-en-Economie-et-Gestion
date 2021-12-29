#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 18:31:46 2021

@author: louisridelle

EXAMEN DIFFICILE - Casier de bieres
"""
class Casier:

    def __init__(self, bac):
        self.__bac=bac

    def party(self, nom):
        for i in self.__bac:
            for j in i:
                if j.estPleine() and j.getNom()==nom:
                    j.boire()

    def avgAlcool(self):
        t=0
        count=0
        for i in self.__bac:
            for j in i:
                if j.estPleine():
                    t+=j.getAlcool()
                    count+=1
        return t/count

    def isStronger(self,tab):
        avgT=self.avgAlcool()
        for i in tab:
            if avgT<=i.avgAlcool():
                return False
        return True