# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:01:18 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

a=input('enter the space seperated number')
b=a.split(' ') 

c=any([True  if int(i)>0 and  i==i[::-1] else False for  i in b] )
 


d=list(map(lambda i:True if int(i)>0 and  i==i[::-1] else False,b))

[False if all(d) else  for i in d]




