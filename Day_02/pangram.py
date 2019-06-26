# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:11:11 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""

str1 ='qwertyuiopasdfghjklzxcvbnm'
l=[]
def Pangram(a):
    for i in str1:
        if i not in a:
            return False
     
    return True

a=input('enter the string')
if Pangram(a)==True:
    print("pangram")
else:
    print("Not pangram")    



def Pangram(a):
    for i in list(range(len(a))):
        if a[i] in str1:
            l.append(a[i])
            
    if len(str1)==len(l):
        print("Pangram")
    else:
        Print("not pangram")
    
    
    
    
    
    
    
    
str1 ='qwertyuiopasdfghjklzxcvbnm'
def Pangram(a):
    for i in str1:
        if i not in a:
            print('Not pangram')
            break
     
    print('Pangram')

a=input('enter the string')
Pangram(a)










    