#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 18:03:02 2021

@author: louisridelle

EXAMEN FACILE - Matrice
"""
def moyenne_diag(M):
    d = [0, 0]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i==j:
                d[0] += M[i][j]
            if -i-1==-j-1:
                d[1] += M[-i-1][j]
    d[0] = d[0]/len(M)
    d[1] = d[1]/len(M)
    return d

def maxima(M):
    l = []
    for i in range(len(M)):
        for j in range(len(M[0])):
            if check_max_loc(M, i, j):
                l.append([i, j])
    return l
    
def check_max_loc(M, i, j):
    if i==0 or i==len(M)-1:
        return False
    elif j==0 or j==len(M[0])-1:
        return False
    else:
        if M[i-1][j] >= M[i][j]: #check en haut
            return False
        if M[i-1][j+1] >= M[i][j]: #check en haut a droite
            return False
        if M[i][j+1] >= M[i][j]: #check a droite
            return False
        if M[i+1][j+1] >= M[i][j]: #check en bas a droite
            return False
        if M[i+1][j] >= M[i][j]: #check en bas
            return False
        if M[i+1][j-1] >= M[i][j]: #check en bas a gauche
            return False
        if M[i][j-1] >= M[i][j]: #check a gauche
            return False
        if M[i-1][j-1] >= M[i][j]: #check en haut a gauche
            return False
    return True