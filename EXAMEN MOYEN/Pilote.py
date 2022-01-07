#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 13:38:19 2022

@author: louisridelle

EXAMEN MOYEN - Pilote
"""
# 4 pilotes et 3 circuits
x = [[[808, 218, 454, 403, 234, 804, 686, 752, 209,  62, 222, 456,  59, 780, 379, 637, 604, 377, 314, 561],
      [347, 613, 592, 723, 899, 467, 868, 683, 755, 102, 869, 846, 260, 291, 304, 192, 454, 493, 216, 854],
      [403, 855, 182,  95,  27, 431, 671, 988, 196, 948,  34, 481,  29, 562, 223,  12, 509, 258, 314, 645]],
     [[624, 586, 516, 785, 347,  66, 344, 450, 997, 235, 976,  24, 611, 710,  60,   2, 122, 256, 432, 543],
      [726, 648, 903, 868, 350, 645, 989, 829,  47, 889, 645, 903, 841, 300, 890, 870, 518,  68, 678, 321],
      [697, 276, 769, 205, 395,  20, 619, 586, 372, 778, 378, 399, 764,  89, 780, 382,  61, 503, 876, 436]],
     [[338, 879,   3, 237, 539,  44, 591, 985,  14, 123, 882, 763, 968, 996, 343, 253, 267, 459, 321, 476],
      [302, 839, 747, 708, 531, 353, 293, 445, 283, 977, 344, 307, 281, 759, 591, 447, 797, 214, 237, 478],
      [905, 728, 163, 932, 687, 827,   9, 648, 508, 242, 348, 711, 216, 377, 446, 902, 643, 118, 378, 264]],
     [[ 76, 357, 765,  76, 312, 540, 899, 476,  12, 863, 624, 372, 819, 777, 550,  43, 784, 522, 765, 234],
      [208, 677, 861, 398,  49, 640, 575, 586, 151, 590, 834, 392, 598, 553, 123, 543,  41, 528, 762, 436],
      [268, 908,  62, 143,  74, 462, 264, 303, 122,   4, 585, 249, 118, 175, 268,  53,  34, 841, 347, 852]]]

def piloteLePlusRapide(x, n):
    win = [0 for i in range(len(x))]
    for race in range(len(x[0])): #iterate on races
        for year in range(n):
            win_time = x[0][race][-year] #To store the index of the winner for each run, each year->begin at pilote 0
            win_pilote = 0 #Store the index of the current winner
            for pilote in range(len(x)): #iterate on pilotes
                if win_time > x[pilote][race][-year] and x[pilote][race][-year]>=0:
                    win_time = x[pilote][race][-year]
                    win_pilote = pilote
            win[win_pilote] += 1
            
    winner = -1 #Find the index of max(win)
    for i in range(len(win)):
        if win[i]>win[winner]:
            winner = i
    return i