#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:56:59 2021

@author: louisridelle

TP06 - EXERCICE 3
"""
"""
Point

"""
import math as m

class Point:

    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    # Méthode pour comparer deux objets Points: A ne pas modifier
    def __eq__(self,autre_point):
        return self.getX()==autre_point.getX() and self.getY()==autre_point.getY() and self.getZ()==autre_point.getZ()

    def translate(self, dx=0, dy=0, dz=0):
        self.setX(self.__x+dx)
        self.setY(self.__y+dy)
        self.setZ(self.__z+dz)
        
    def distance(self, p):
        return m.sqrt((self.getX()-p.getX())**2 + (self.getY()-p.getY())**2 + (self.getZ()-p.getZ())**2)
    
    """
    GETTER
    """
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getZ(self):
        return self.__z
    
    """
    SETTER
    """
    def setX(self, a):
        self.__x = a
        
    def setY(self, a):
        self.__y = a
        
    def setZ(self, a):
        self.__z = a

    #A ne pas modifier
    def __str__(self):
        return "x: {} y: {} z: {}".format(self.getX(),self.getY(),self.getZ())
    
p1 = Point(1, 2, 3)
print(p1)

