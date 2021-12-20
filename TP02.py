#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:12:31 2021

@author: louisridelle

TP02 - Inginious exercices 
"""
"""
EXERCICE 1 - Pair

"""
def pair(nbr):
    if nbr<=2:
        return 0
    sum=0
    for i in range(2,nbr):
        if i%2==0:
            sum+=i
            print(i, end =' ')
    print()
    return sum

"""
EXERCICE 2 - Etoiles

"""
def carre(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("")
        
def triangle1(n):
    for i in range(n):
        for j in range(i+1):
            if n==1 or i==j:
                print('*', end='')
            else:
                print('*', end=' ')
        print(' ')

def triangle2(n):
    if n==1:
        print('* ')
    else:
        for i in range(n):
            print(' ' * 2*(n-1-i), end='')
            print('* ' * (i+1))
    

"""
EXERCICE 3 - Factorielle

"""
def fact(n):
    if n==0:
        return 1
    mult=1
    for i in range(1,n+1):
        mult=mult*i
    return mult

"""
EXERCICE 4 - Fibonacci

"""
def fibo(n):
    if n==0 or n==1:
        return n
    if n<=0:
        return 0
    return fibo(n-1)+fibo(n-2)

"""
EXERCICE 5 - Distance Terre Lune

"""
import math as ma

def distance(m):
    if(m<=0):
        return 0
    return ma.ceil(ma.log(384400000000/m, 2))

"""
TESTS

"""
ex = input("Quel exos ? ")

#if ex=='1':
    
#if ex=='2':
    
#if ex=='3':
    
#if ex=='4':
    
#if ex=='5':