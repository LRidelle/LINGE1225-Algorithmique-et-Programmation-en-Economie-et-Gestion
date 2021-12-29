#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:15:50 2021

@author: louisridelle

EXAMEN FACILE - Modularite
"""
A = [[0, 1, 2],
     [1, 0, 3],
     [2, 3, 0]]

def calculModularite(A):
    d, tot = deg_sum(A)
    Q = [[0 for i in range(len(A))] for j in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            Q[i][j] = A[i][j] - (d[i]*d[j]/tot)
    return Q

#Fonction qui calcul le vecteur d et la somme totale de A
def deg_sum(A):
    d = [0 for i in range(len(A))]
    tot = 0
    for i in range(len(A)):
        for j in range(len(A[0])): #d[i]=sum(A[i]) fait pareil
            d[i] += A[i][j]
            tot += A[i][j]
    return d, tot #tot=sum(d) fait pareil

print(deg_sum(A))
print(calculModularite(A))