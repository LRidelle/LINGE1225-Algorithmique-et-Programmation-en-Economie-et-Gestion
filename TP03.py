#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:16:20 2021

@author: louisridelle

TP03 - Inginious exercices 
"""
"""
EXERCICE 1 - Nombre de mots

"""
def nbr_mot(string):
    count=0
    if(string==" "):
        return count
    space=True
    for i in string:
        if(i==" " and space):
            space=False
            count+=1
        elif(i!=" "):
            space=True
    return count+1

"""
EXERCICE 2 - Anagramme

"""
def anagramme(str1, str2):
    if len(str1)!=len(str2):
        return False
    if str1==str2:
        return True
    for i in str1:
        if i not in str2:
            return False
    return True

"""
EXERCICE 3 - Chaines de caractères

"""
def change(str):
    return str.replace("r", "l")

def change_sup(str, lettre1, lettre2):
    return str.replace(lettre1, lettre2)

"""
EXERCICE 4 - Miroir

"""
def miroir(string):
    return string[::-1]

"""
EXERCICE 5 - Multiple

"""
def verifierMul(l, n):
    if n==0:
        return False
    for i in l:
        if i%n!=0:
            return False
    return True

"""
EXERCICE 6 - Merge two lists

"""
def merge_two_lists(lst1, lst2):
    if lst1==[]:
        return lst2
    if lst2==[]:
        return lst1
    return sorted(lst1+lst2)

"""
TESTS

"""
ex = input("Quel exos ? ")

if ex=='1':
    
if ex=='2':
    
if ex=='3':
    
if ex=='4':
    
if ex=='5':
    
if ex=='6':