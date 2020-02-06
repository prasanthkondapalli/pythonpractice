# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:14:08 2020

@author: Prasanth
"""

a= int(input('enter the number a= >>'))
b=int(input('enter the number b= >>'))
print(f' before swaping the numbers a={a} and b={b}')
a=a^b
b=a^b
a=a^b
print(f' after swaping the numbers a={a} and b={b}')
