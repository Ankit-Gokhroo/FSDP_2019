# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:25:14 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
    
  Input:
      orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
                 [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                 [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                 [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] 
               ]
     
  Output:
       [[1, 678.33], [2, 494.46], [3, 364.8], [4, 492.57]]     

"""


orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
                 [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                 [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                 [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] 
               ]


   
list1=[]
for i in orders:
    a=i[0]
    b=i[1:]
    for j in b:
        list1.append([a,list(j)[1] * list(j)[2]])
        
         
d={}        
        
        
        
for i in list1:
        d[i[0]] = d.get(i[0], 0) +  i[1] 
        #print(dict1)
        if(d[i[0]] < 100):
             print((i[0],d[i[0]]))
        else:
          print(d)          
        
        
        
    

for new in invoice:
        dict1[new[0]] = dict1.get(new[0], 0) +  new[1] 
        #print(dict1)
        if(dict1[new[0]] < 100):
             print((new[0],dict1[new[0]]))
        else:
          print(dict1)  






