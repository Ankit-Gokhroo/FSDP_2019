# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:04:46 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

  Input:
    orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]
  Output:
      [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
      

"""

orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

l1=[]

for i in orders:
    if i[-1]*i[-2] <100:
        
        l1.append((i[0],i[-1]*i[-2]+10))
    else:
        l1.append((i[0],i[-1]*i[-2]))
        
        


[(i[0],i[-1]*i[-2]+10) if i[-1]*i[-2] <100  else (i[0],i[-1]*i[-2] )    for i in orders ]


z=list(map(lambda i:(i[0],i[-1]*i[-2]+10) if i[-1]*i[-2] <100  else (i[0],i[-1]*i[-2] ),orders))











