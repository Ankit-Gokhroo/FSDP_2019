# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:00:32 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

x=int(input('enter the value whose factorial you want'))

#importing module math which is collection of many functions
import math

#use dir function to check all the functions present in the particular module
dir(math)

#use help function to find details of particular function of the module
help(math.factorial)

#factorial function gives factorial value
factorial_value=math.factorial(x)
