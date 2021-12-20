#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:06:20 2021

@author: louisridelle

EXAMEN FACILE - Integrale
"""
def identite(x):
    return x

def carre(x):
    return x*x

def integrale(a,b,nbPoints, fonc):
    aire = 0
    x = []
    delta = (b-a)/(nbPoints-1)
    for i in range(nbPoints):
        x.append(a + i * delta)
        
    for i in range(len(x)-1):
        aire += 1/2 * (x[i+1] - x[i]) * (fonc(x[i]) + fonc(x[i+1]))
    return aire