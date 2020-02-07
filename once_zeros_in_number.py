# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:18:58 2020

@author: Prasanth
"""

a=int(input('enter the number >>'))
a1=bin(a)
a1=list((a1[2:]))
print('zeros in a given number',a1.count('0'))
print('once in a given number',a1.count('1'))