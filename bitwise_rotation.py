# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:29:43 2020

@author: Prasanth
"""

a=int(input('enter the number >>'))
a1=bin(a)
a1=list((a1[2:]))
r=int(input('enter the rotations>>'))
a2=a1[r::]+a1[:r]
print('before the rotation',a1)
print('after the rotaion',a2)