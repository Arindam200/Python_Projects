# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:46:02 2022

@author: INAKKAM
"""

str1 = "x + 30 = 53"
a = []
for ele in str1.split():
        a.append(ele)
        
a1=a[0]
op=a[1]
b=a[2]
c=a[4]

if ele in a:
    if ele.find('x'):
        if op =="+":
            new_a=int(c)-int(b)
        if op =="-":
            new_a=b+c
        if op =="*":
            new_a=c/b
        if op =="/":
            new_a=c*b
        new_a1=str(new_a)
    if a1!='x':
        for i in range(len(a1)):
            if a1[i]=='x':
                x=new_a1[i]
    else:
        x=new_a
print(x)