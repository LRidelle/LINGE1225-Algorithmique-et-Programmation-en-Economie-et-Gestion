#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:20:06 2021

@author: louisridelle

TP04 - Inginious exercices 
"""
"""
EXERCICE 1 - Demi somme

"""
def demiSomme(mat):
    if len(mat)!=len(mat[0]):
        return None
    tab=[]
    for i in range(len(mat)):
        sum=0
        for j in range(i,len(mat)):
            sum+=mat[i][j]
        tab.append(sum)
    return tab

"""
EXERCICE 2 - Carre magique

"""
def estMagique(mat):
    if len(mat)!=len(mat[0]):
        return False
    n=len(mat)
    val=[]
    diag=0
    adiag=0
    for i in range(n):
        line=0
        for j in range(n):
            line+=mat[i][j]
            if i==j:
                diag+=mat[i][j]
            if i+j==n-1:
                adiag+=mat[i][j]
        val.append(line)
    val.append(diag)
    val.append(adiag)
    for i in range(len(val)-1):
        if val[i]!=val[i+1]:
            return False
    return True

"""
EXERCICE 2 - Taxi&Run

"""
def payeTaxi(M, P):
    if M==[] or P==0:
        return [0, 0]
    max=0
    cMax=0
    tot=0
    for i in M:
        d=(abs(i[3]-i[1]))+abs((i[4]-i[2]))
        tot+=d*P
        if i==M[0]:
            cMax=i[0]
            max=d*P
        if max<d*P:
            cMax=i[0]
    return [tot, cMax]

"""
EXERCICE 4 - Meteo par regions

"""
def meteo(lst1, lst2):
    lst = [[0 for i in range(len(lst1))] for j in range(len(lst1))]
    for i in range(len(lst2)):
        for j in range(len(lst2[0])):
            lst[lst1[i][j][0]][lst1[i][j][1]] = lst2[i][j]

"""
EXERCICE 5 - Average beers

"""
def average(mat):
    pers = [0 for i in range(len(mat[0]))]
    soiree = [0 for i in range(len(mat))]
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            pers[j] += mat[i][j]# / len(mat)
            soiree[i] += mat[i][j]# / len(mat[0])
            
    for i in range(len(pers)):
        pers[i] = pers[i]/len(mat)
        
    for i in range(len(soiree)):
        soiree[i] = soiree[i]/len(mat[0])
    return [pers, soiree]

"""
EXERCICE SUPP 1 - Matrice identité

"""
def matriceIdentite(n):
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                mat[i][j]=1
    return mat

"""
EXERCICE SUPP 2 - Max matrice

"""
def maxmatrice(mat):
    max = mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] >= max:
                max = mat[i][j]
    return max

"""
EXERCICE SUPP 3 - Sommes colonnes

"""
def colsomme(mat):
    somme = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==0:
                somme.append(mat[i][j])
            else:
                somme[j] += mat[i][j]
    return somme

"""
TESTS

"""
ex = input("Quel exos ? ")

if ex=='1':
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    assert demiSomme(m)==[6, 11, 9]
    print(demiSomme(m))
    
if ex=='2':
    m = [[4, 9, 2],
         [3, 5, 7],
         [8, 1, 6]]
    assert estMagique(m)==True
    print(estMagique(m))
    
if ex=='3':
    m = [[1, -6, -3, 3, -5], [2, 1, 9, -1, 4], [3, 2, 3, 1, 3], [4, 2, -4, -5, -10]]
    assert payeTaxi(m, 9)==[288, 4]
    print(payeTaxi(m, 9))
    
if ex=='4':
    m1 = [[[1,0],[0,1]],[[1,1],[0,0]]]
    m2 = [[20, 18],[17, 16]]
    assert meteo(m1, m2)==[[16, 18], [20,17]]
    print(meteo(m1, m2))
    
if ex=='5':
    m = [[2,4,6,8],[1,3,5,7]]
    assert average(m)==[[1.5, 3.5, 5.5, 7.5], [5.0, 4.0]]
    print(average(m))