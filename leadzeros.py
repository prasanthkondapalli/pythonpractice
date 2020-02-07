# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:32:00 2020

@author: Prasanth
"""

a=int(input('enter the number >>'))
b=int(input('enter the number >>'))

a1=bin(a)
b1=bin(b)
a1=list((a1[2:]))
b1=list((b1[2:]))
x=0
y=0
x=a1.count('0')
y=b1.count('0')

if x<y:
	print('b has heighest zeros',b1 )
elif x>y:
	print('a has heighest zeros',a1)
else:
	print('both  has equal zeros',a1,b1)

