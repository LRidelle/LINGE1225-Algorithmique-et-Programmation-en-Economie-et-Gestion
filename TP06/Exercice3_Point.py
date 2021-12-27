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
        self.x = x
        self.y = y
        self.z = z

    def translate(self, dx=0, dy=0, dz=0):
        self.setX(self.x+dx)
        self.setY(self.y+dy)
        self.setZ(self.z+dz)
        
    def distance(self, p):
        return m.sqrt((self.getX()-p.getX())**2 + (self.getY()-p.getY())**2 + (self.getZ()-p.getZ())**2)

    """
    GETTER
    """
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    
    """
    SETTER
    """
    def setX(self, a):
        self.x = a
        
    def setY(self, a):
        self.y = a
        
    def setZ(self, a):
        self.z = a

    #A ne pas modifier
    def __str__(self):
        return "x: {} y: {} z: {}".format(self.getX(),self.getY(),self.getZ())
    
    # Méthode pour comparer deux objets Points: A ne pas modifier
    def __eq__(self,autre_point):
        return self.getX()==autre_point.getX() and self.getY()==autre_point.getY() and self.getZ()==autre_point.getZ()
    
p1 = Point(1, 2, 3)
print(p1)

