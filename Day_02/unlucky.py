# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:38:59 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""

a=[]
sum=0
numbers= (input("Enter a numbers "))
alist = numbers.split()

for i in alist:
    if i=='13':
        ind=alist.index(i)
        del alist[ind]
        del alist[ind+1]
    else:
        pass
for j in alist:
    sum=sum+int(j)
    print(sum)
        
    
    
    
        