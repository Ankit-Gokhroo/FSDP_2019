# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:52:42 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

str1=input('enter the string')

dict1={}
dict1['Letters']=0
dict1['Digits']=0
a='qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOPQRSTUVWXYZ'
d='1234567890'
for i in str1:
    if i in a:
        dict1['Letters']=dict1['Letters']+1
    elif i in d:
        dict1['Digits']=dict1['Digits']+1
    else:
        pass
    


for k,v in dict1.items():
    print(k,v)
    
