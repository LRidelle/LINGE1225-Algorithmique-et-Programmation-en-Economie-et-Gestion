#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:16:47 2021

@author: louisridelle

MONITORATS - Inginious exercices 
"""
"""
01

"""
def premiers(n):
    l = []
    if n <= 0:
        return l
    l.append(2)
    if len(l)==n:
        return l
        return l
    for j in range(2, 3571):
        i=2
        while i < j and j % i != 0 :
            i = i + 1
            if i == j :
                l.append(j)
                if len(l)==n:
                    return l

"""
02.1

"""
def dist_euclidienne_indiv(M):
    mat = [[0]*len(M[0])] * len(M)
                