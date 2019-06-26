# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:37:14 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
a=[11,47,9]
count = 0
for i in a:
    if int(i) > 0:
        if  i[count]==i[count][::-1]:
            count=count+1
    print("True")   
    
    
    
            
            
            
            
        
       
            
   