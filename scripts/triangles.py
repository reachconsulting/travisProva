#!/usr/bin/env python 
#
#        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                    Version 2, December 2004 
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 
#
# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#
from __future__ import division
from math import floor, sqrt

#from numpy.distutils.fcompiler import none


class Triangle:
    a = 0
    b = 0
    c = 0
    def __init__(self, l, m, n):
        self.a = l
        self.b = m
        self.c = n
        if not self.isTriangle():
            raise ValueError('Not a triangle') 


    def calcArea(self):
        p = self.calcPerimeter()/2
        print p
        area = sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        print area
        return area
        
    def calcPerimeter(self): 
        return self.a+self.b+self.c

    def isTriangle(self):
        return (self.a + self.b > self.c) and (self.a +self.c > self.b) and (self.c +self.b > self.a)

    def isEquilateral(self):
        #Correct
        #return (self.a == self.b) and (self.b == self.c) and (self.c == self.a)
        # EPIC FAIL
        avg = (self.a + self.b + self.c) / 3
        return (self.a == avg)
    


class Equilateral(Triangle):
    
    def __init__(self, l):
        self.a = l
        self.b = l
        self.c = l
                    
    def isEquilateral(self):
        return True


def main():
    anyTriangle = Triangle(3,2,4)
    print 'area = ' +  str(anyTriangle.calcArea())
    print 'perimeter ' + str(anyTriangle.calcPerimeter())
 
 
if __name__ == "__main__":
    main()
