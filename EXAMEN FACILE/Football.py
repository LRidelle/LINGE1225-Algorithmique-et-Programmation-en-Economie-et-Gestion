#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:30:59 2021

@author: louisridelle

EXAMEN FACILE - Football
"""
import math

but = [['X' for i in range(10)] for j in range(5)]
but[12][7] = 'B'
but[0][5] = 'G'

def arret(but):
    dL, dH, direc = donnee(but)
    if dL == 0.:
        return 0., 90., dH
    elif dH == 0:
        return direc, 0., dL
    else:
        angle = math.atan(dH/dL)
        dist = math.sqrt(dH*dH + dL*dL)
        return direc, angle*180/math.pi, dist

#Fonction qui renvoie les donnees necessaire au probleme (dH et dL)
def donnee(but):
    lG = 0.
    lB, hB = 0., 0.
    for i in range(len(but)):
        for j in range(len(but[0])):
            if but[i][j]=='G':
                lG = j
            if but[i][j] == 'B':
                lB, hB = j, i
    direc = 0.
    dH = hB
    dL = lG - lB
    if dL < 0:
        direc = -1.
        dL = -dL
    elif dL == 0:
        direc = 0.
    elif dL > 0:
        direc = 1.
    return dL, dH, direc