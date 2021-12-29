#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:24:17 2021

@author: louisridelle

TP05 - Inginious exercices 
"""
"""
EXERCICE 1 - Abreviation

"""
def remplace(message, abreviation):
    arr = []
    if message=='':
        print(message)
        return
    for i in range(len(message.split(' '))):
        tab = message.split()
        if tab[i] in abreviation:
            arr.append(abreviation.get(tab[i]))
    print(' '.join(arr))
    
"""
EXERCICE 2 - Country

"""
def get_country(l, name):
    for i in range(len(l)):
        if l[i]["City"]==name:
            return l[i]["Country"]
    return False

"""
EXERCICE 3 - Prediction de mots

"""
def predic(lst, mot):
    dico = {}
    for i in range(len(lst)):
        tab = lst[i].split()
        for j in range(len(tab)):
            #tab[j] = "".join(u for u in tab[j] if u not in ("?", ".", ";", ":", "!", ","))
            if tab[j]==mot and not j==len(tab)-1 and tab[j+1] not in dico:
                dico[tab[j+1]] = 1
            elif tab[j]==mot and not j==len(tab)-1 and tab[j+1] in dico:
                dico[tab[j+1]] = dico[tab[j+1]] + 1
    return dico

"""
EXERCICE 4 - Nombre de messages (FAUX)

"""
l = [["Grumpy", "Garfield"],["Grumpy", "Lucifer"],["Lucifer", "Grumpy"],
     ["Garfield", "Grumpy"],["Garfield", "Grumpy"],["Garfield", "Grumpy"]]

def message(lst):
    dicos = []
    for i in lst:
        already_in_dicos = False
        for dic in dicos:
            if i[0] == dic['Auteur']:
                if i[1] in dic:
                    dic[i[1]] += 1
                else:
                    dic[i[1]] = 1
                already_in_dicos = True
        if not already_in_dicos:
            new_dico = {}
            new_dico['Auteur'] = i[0]
            new_dico[i[1]] = 1
            dicos.append(new_dico)
    return dicos

print(message(l))

"""
EXERCICE 5 - Position d une lettre dans un mot

"""
l = ["bonjour","bonsoir", "cours","partir","clavier","souris", "tests", "ordinateur"]
l2 = ['bonjour', 'bonsoir', 'cours', 'partir', 'clavier', 'souris', 'tests',
      'ordinateur', 'inginious', 'informatique', 'chargeur', 'téléphone',
      'feuille', 'cuisine', 'maison', 'ballon', 'table', 'canapé', 'chaise',
      'sport', 'football', 'voiture', 'vélo']

def position(lst, lettre):
    dico = {}
    if lst==[]:
        return dico
    for i in range(len(lst)):
        tab = [pos for pos, char in enumerate(lst[i]) if char == lettre]
        for j in range(len(tab)):
            if not tab[j] in dico:
                dico[tab[j]] = [lst[i]]
            else:
                dico[tab[j]].append(lst[i])
    return dico

"""
EXERCICE SUPP 1 - Dictionnaires esperance de vie

"""

"""
EXERCICE SUPP 2 - Dictionnaires nuage de mots

"""
def compte_mots(phrase, speciaux):
    dico = {}
    tab = phrase.split()
    for i in range(len(tab)):
        if tab[i] not in speciaux:
            if tab[i] not in dico:
                dico[tab[i]] = 1
            else:
                dico[tab[i]] += 1
    return dico

"""
EXERCICE SUPP 3 - Creation de dictionnaires

"""
def create_dict(l):
    dico = {}
    for i in range(len(l)):
        if l[i][0] not in dico:
            dico[l[i][0]] = [l[i][1]]
        else:
            dico[l[i][0]].append(l[i][1])
    return dico

"""
EXERCICE SUPP 4 - IMC

"""
def IMC(patients):
    labels = {"maigreur": [],
              "normal":   [],
              "surpoids": [],
              "obésité":  [] }
    for nom, values in patients.items():
        IMC = 10000 * values[1]/(values[0]*values[0])
        if IMC < 18.5:
            labels["maigreur"].append(nom)
        elif IMC < 25:
            labels["normal"].append(nom)
        elif IMC < 30:
            labels["surpoids"].append(nom)
        else:
            labels["obésité"].append(nom)
    return labels

"""
EXERCICE SUPP 5 - Banques

"""
def Transfert(banque1, banque2):
    dico = banque1
    for k, v in banque2.items():
        if k in banque1:
            dico[k] += banque2[k]
        else:
            dico[k] = banque2[k]
    return dico

"""
EXERCICE SUPP 6 - Cumul mandats

"""
def cumul(mandats):
    l = []
    lst = []
    for v in mandats.values():
        lst += v
    for n in lst:
        if lst.count(n) > 1 and n not in l:
            l.append(n)
    return l
