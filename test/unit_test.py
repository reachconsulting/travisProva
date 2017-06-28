#
# UNLICENSE
#
# This is free and unencumbered software released into the public domain.
# 
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# 
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# Author: alessandro_DOT_mortari_AT_gmail_DOT_com
#


import sys
import io
import unittest
import mock
from scripts.triangles import *
from __builtin__ import ValueError

class TestTriangle(unittest.TestCase):
 
    def test_null(self):
        with self.assertRaises(ValueError):
            sut = Triangle(0,0,0)

    def test_border1(self):
        with self.assertRaises(ValueError):
            sut = Triangle(1,2,3)           

    def test_border2(self):
        with self.assertRaises(ValueError):
            sut = Triangle(3,2,1)           

    def test_border3(self):
        with self.assertRaises(ValueError):
            sut = Triangle(1,3,2)           

    def test_border4(self):
        with self.assertRaises(ValueError):
            sut = Triangle(2,3,1)           

    def test_greater1(self):
        with self.assertRaises(ValueError):
            sut = Triangle(1,2,8)      

    def test_greater2(self):
        with self.assertRaises(ValueError):
            sut = Triangle(1,8,2)  

    def test_greater3(self):
        with self.assertRaises(ValueError):
            sut = Triangle(1,8,2)  

    def test_perimeter(self):
        sut = Triangle(2,3,2)
        assert(sut.calcPerimeter()>0)
 
    def test_area(self):
        sut = Triangle(2,3,2)
        assert(sut.calcArea()>0)
    
    def test_equilateral1(self):
        sut = Triangle(4,6,4) #isosceles
        self.assertFalse(sut.isEquilateral())

    def test_equilateral2(self):
        sut = Triangle(5,6,4) #scalene
        self.assertFalse(sut.isEquilateral())                 
           
    def test_equilateral3(self):
        sut = Triangle(5,5,5) #equilateral
        self.assertTrue(sut.isEquilateral())  
    
 