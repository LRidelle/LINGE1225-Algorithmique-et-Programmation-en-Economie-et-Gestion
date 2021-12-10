#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:59:17 2021

@author: louisridelle

TP01 - Inginious exercices 
"""
"""
EXERCICE 1 - Heure

"""
def heure(nbr_seconde):
    heure=int(nbr_seconde/3600)
    minute=int((nbr_seconde - heure*3600)/60)
    seconde=int(nbr_seconde - heure*3600 - minute*60)
    print(str(heure)+" heures, "+str(minute)+" minutes et "+str(seconde)+" secondes")
    
"""
EXERCICE 2 - Moyenne

"""
def moyenne(a, b):
    return (a+b)/2

def main():
    a=input("Entrez le premier nombre :")
    b=input("Entrez le deuxième nombre :")
    print("La moyenne est : "+str(moyenne(a, b)))
    
"""
EXERCICE 3 - Volume et surface d une sphère

"""
import math as m

def volume(r):
    return (4/3)*m.pi*r*r*r

def surface(r):
    return 4*m.pi*r*r

"""
EXERCICE 4 - Maximum

"""
def max():
    a=input("Entrez le numero 1 :")
    b=input("Entrez le numero 2 :")
    c=input("Entrez le numero 3 :")
    if a>=b and a>=c:
        print("Le nombre le plus grand est "+str(a))
        if a==b or a==c:
            print("Mais vous avez introduit des valeurs identiques !")
    elif b>=a and b>=c:
        print("Le nombre le plus grand est "+str(b))
        if b==a or b==c:
            print("Mais vous avez introduit des valeurs identiques !")
    elif c>=a and c>=b:
        print("Le nombre le plus grand est "+str(c))
        if c==a or c==b:
            print("Mais vous avez introduit des valeurs identiques !")
        
"""
EXERCICE 5 - Police

"""
def amende(vmax, v):
    amende=0.0
    diff=v-vmax
    if(diff>0 and diff<10):
        amende=diff*5
        if(amende<12.5):
            return 12.5
        return amende
    if(diff>10):
        amende=diff*5*2
        return amende
    return amende